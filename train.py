# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:05:26 2019

@author: ryan4
"""

import matplotlib.pyplot as plt
from build_model import build_model
from data_processing import get_training_data

def train(intents_file_path, emb_dim, num_epochs, train=True, show_training_results=False):
    
    training_set, training_labels, word_count, max_sequence_len = get_training_data(intents_file_path)
    
    model = build_model(word_count,emb_dim,max_sequence_len,len(training_labels))
    
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=["accuracy"])
    
    model.summary()

    if train == False:
        return model
    
    history = model.fit(training_set, training_labels, 
                        epochs=num_epochs, 
                        shuffle=True,
                        verbose=1)
    
    model.save('HueWeights.h5')
   
    if show_training_results == True:
        #Plot training loss
        acc = history.history['accuracy']
        loss = history.history['loss']
        
        epochs = range(len(acc))
        
        plt.plot(epochs, acc, 'b', label='Training accuracy')
        plt.title('Training accuracy')
        
        plt.figure()
        
        plt.plot(epochs, loss, 'b', label='Training Loss')
        plt.title('Training loss')
        plt.legend()
        
        plt.show()
        
train('my_intents.json',256,50)