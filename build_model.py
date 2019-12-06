# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:58:15 2019

@author: ryan4
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, GlobalAveragePooling1D

def build_model(total_words, emb_dim, max_seq_len,num_classes):
    model = Sequential()
    
    model.add(Embedding(total_words, emb_dim, input_length=max_seq_len))
    model.add(GlobalAveragePooling1D())
    model.add(Dense(num_classes*4, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    
    return model