# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:59:43 2019

@author: ryan4
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import json

def get_training_data(intents_file_path):
    
    try:
        with open('token_data.pickle','rb') as f:
            training_set, training_labels, word_count, max_sequence_len = pickle.load(f)
            
        return training_set, training_labels, word_count, max_sequence_len 
    
    except:
    
        with open(intents_file_path) as f:
            data = json.load(f)
            
        #Parse the data
        sentences = []
        labels = []
        sentences_y = []
        
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                sentences.append(pattern)
                sentences_y.append(intent["tag"]) #So we have a tag associated with the pattern
                
            if intent["tag"] not in labels:
                labels.append(intent["tag"])
        
        #Create tokenizer
        tokenizer = Tokenizer(oov_token="<OOV>")
        tokenizer.fit_on_texts(sentences)
        word_count = len(tokenizer.word_index) + 1
        
        #print(tokenizer.word_index)
        
        #Tokenize and pad
        sequences = tokenizer.texts_to_sequences(sentences)
        max_sequence_len = max([len(x) for x in sequences])
        padded_sequences = pad_sequences(sequences,maxlen=max_sequence_len,truncating='post')
        
        #Label tokenizer
        label_tokenizer = Tokenizer()
        label_tokenizer.fit_on_texts(labels)
        
        tok_labels = np.array(label_tokenizer.texts_to_sequences(sentences_y))
        
        training_labels = np.zeros((padded_sequences.shape[0],len(labels)))
        
        for i in range(padded_sequences.shape[0]):
            training_labels[i][tok_labels[i]-1] = 1
        
        with open('token_data.pickle','wb') as f:
            pickle.dump((padded_sequences, training_labels, word_count, max_sequence_len), f)

        with open('raw_data.pickle','wb') as f:
            pickle.dump((sentences, labels, sentences_y), f)
        
        return padded_sequences, training_labels, word_count, max_sequence_len 