# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:38:01 2019

@author: ryan4
"""

import yaml
import json

#Processing files
start_path = '/The-Hue-Chatbot/Conversations/'
topics = ['ai','botprofile','computers','emotion','food','gossip','greetings','health',
         'history','humor','literature','money','movies','politics','psychology',
          'science','sports','trivia']

with open('my_intents.json') as file:
    data = json.load(file)

tags = []
existing_dict = {}
for intent in data["intents"]:
    tags.append(intent['tag'])
    existing_dict[intent['tag']] = intent

#pattern, response = [], []
context_set = ""
for topic in topics:
    filepath = "%s%s.yml" % (start_path,topic)
    with open(filepath) as file:
        chat = yaml.load(file, Loader=yaml.FullLoader)
    chat = chat["conversations"]
    
    for line in chat:
        pattern = line[0]
        print(pattern)
    
        inp = input("Tag: ")
        
        if len(line) == 2:
            response = line[1]
            
            if inp in existing_dict.keys():
                print("Existing Tag")
                #if pattern not in existing_dict[inp]["patterns"]: 
                existing_dict[inp]["patterns"].append(pattern) #Multiple entries for eventual cosine similarity
                #if response not in existing_dict[inp]["responses"]:
                existing_dict[inp]["responses"].append(response) #Multiple entries for eventual cosine similarity
            else:
                print("New tag")
                new_entry = {'tag' : inp,
                             'patterns' : [pattern],
                             'responses' : [response],
                             'context_set' : context_set}
                data["intents"].append(new_entry)
                existing_dict[inp] = new_entry            
        
        else: #More than one response
            for i in range(1,len(line)):
                response = line[i]
                
                if inp in existing_dict.keys():
                    print("Existing Tag")
                    #if pattern not in existing_dict[inp]["patterns"]: 
                    existing_dict[inp]["patterns"].append(pattern) #Multiple entries for eventual cosine similarity
                    #if response not in existing_dict[inp]["responses"]:
                    existing_dict[inp]["responses"].append(response) #Multiple entries for eventual cosine similarity
                else:
                    print("New tag")
                    new_entry = {'tag' : inp,
                                 'patterns' : [pattern],
                                 'responses' : [response],
                                 'context_set' : context_set}
                    data["intents"].append(new_entry)
                    existing_dict[inp] = new_entry
                    
new_data = {}
dict_as_list = []
for key in existing_dict.keys():
    dict_as_list.append(existing_dict[key])
    
new_data["intents"] = dict_as_list
        
with open("my_intents.json", "w") as f:
    json.dump(new_data, f, indent=4, sort_keys=True)
        
        
        