# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:10:26 2019

@author: ryan4
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from data_processing import get_training_data
from train import train

import numpy as np
import pickle
import random
import json

def chat(intents_file_path):
    
    with open(intents_file_path) as f:
        data = json.load(f)
    
    model = train(intents_file_path, 256, 50, train=False) 
    
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
    
    print("Start talking with the bot (type quit to stop)!")
    
    tokenizer = Tokenizer(oov_token="<OOV>")
    tokenizer.fit_on_texts(sentences)
    
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
        
        print(random.choice(responses))