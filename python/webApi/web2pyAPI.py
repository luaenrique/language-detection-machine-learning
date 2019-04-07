import nltk
import random
import os
import pickle
import json
import requests
import urllib.request

def returnLanguage():
    #defining headers: 
    response.headers["Access-Control-Allow-Origin"] = '*'

    #getting the classifier
    classifier_f = open("naivebayes4.pickle","rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()
    
    #receiving GET data ?text='something'
    words = request.vars.text
    
    dictio = dict([(word, True) for word in words.lower().split()])
    language = classifier.classify(dictio)
    return response.json({'texto': words, 'language': language})
