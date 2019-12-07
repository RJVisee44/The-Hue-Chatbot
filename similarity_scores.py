# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:26:41 2019

@author: ryan4
"""
import numpy as np
import math

"""
def remove_stopwords(sentence):
    stopwords = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
        
    sent = [w for w in sentence.lower().split() if not w in stopwords]
    
    return sent
"""

def sum_word_vectors(sentence, embeddings_dict):
    sent_vector = 0
    #sentence = remove_stopwords(sentence)
    for word in sentence.lower().split():
        if word not in embeddings_dict.keys() :
            word_vector = np.array(np.random.uniform(-1.0, 1.0, 50))
            embeddings_dict[word] = word_vector
        else:
            word_vector = embeddings_dict[word]
        sent_vector = sent_vector + word_vector

    return sent_vector 

def cosineValue(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def most_similar(input_sentence, patterns, embeddings_dict):
    similarity_score = []
    inp_sent_vect = sum_word_vectors(input_sentence,embeddings_dict)
    for sentence in patterns:
        sentence_vect = sum_word_vectors(sentence,embeddings_dict)
        similarity_score.append(cosineValue(inp_sent_vect,sentence_vect))
        
    max_similarity = max(similarity_score)
    max_sim_ind = [i for i, j in enumerate(similarity_score) if j == max_similarity]
    
    return max_sim_ind
        