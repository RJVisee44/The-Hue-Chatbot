# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:10:26 2019

@author: ryan4
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from data_processing import get_training_data
from train import train
<<<<<<< HEAD
from similarity_scores import most_similar
=======
>>>>>>> b7b37c2e9daa27edbcf1e0c1730b2e4a8d779779

import numpy as np
import pickle
import random
import json

def chat(intents_file_path):
    
    with open(intents_file_path) as f:
        data = json.load(f)
    
    model = train(intents_file_path, 256, 50, train=False) 
<<<<<<< HEAD
    model.load_weights('HueWeights.h5')
=======
>>>>>>> b7b37c2e9daa27edbcf1e0c1730b2e4a8d779779
    
    try:
        with open('raw_data.pickle','rb') as f:
            sentences, labels, sentences_y = pickle.load(f)        
    except:
        print("raw_data.pickle does not exist, please run data_processing.py")
        return 0
    
    try:
        with open('token_data.pickle','rb') as f:
            training_set, training_labels, word_count, max_sequence_len = pickle.load(f)
    except:
        training_set, training_labels, word_count, max_sequence_len = get_training_data(intents_file_path)
    
<<<<<<< HEAD
    tokenizer = Tokenizer(oov_token="<OOV>")
    tokenizer.fit_on_texts(sentences)
    
    embeddings_dict = {}
    with open('glove.6B.50d.txt', 'r', encoding="utf8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], "float32")
            embeddings_dict[word] = vector    
    
    print("Start talking with the bot (type quit to stop)!")
    
=======
    print("Start talking with the bot (type quit to stop)!")
    
    tokenizer = Tokenizer(oov_token="<OOV>")
    tokenizer.fit_on_texts(sentences)
    
>>>>>>> b7b37c2e9daa27edbcf1e0c1730b2e4a8d779779
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        token_list = tokenizer.texts_to_sequences([inp])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len, padding='post')
        predicted = model.predict(token_list)
        
        result_ind = np.argmax(predicted)
        
        tag = labels[result_ind] #Returns the tag it thinks the tag is
        
        for tg in data["intents"]:
            if tg['tag'] == tag:
                print(tag)
                responses = tg['responses']
<<<<<<< HEAD
                patterns = tg['patterns']
        
        #Get best response
        max_sim_ind = most_similar(inp, patterns, embeddings_dict)
        
        if len(max_sim_ind) > 1:
            print(responses[random.choice(max_sim_ind)])
        else:
            print(responses[max_sim_ind[0]])

chat('my_intents.json')     
=======
        
        print(random.choice(responses))
>>>>>>> b7b37c2e9daa27edbcf1e0c1730b2e4a8d779779
