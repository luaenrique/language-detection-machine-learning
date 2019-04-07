import nltk
import random
import os
import pickle

def generateDocuments(direcSelected):
     documents = []
               
     for i in range(len(direcSelected)):
          direc = direcSelected[i]
          files = os.listdir(direc)
              
          sentences = [direc + sentence for sentence in files]

          words = []
         
          for sentence in sentences:
               count = 0
               f = open(sentence, encoding="utf-8")
               for x in f:
                   words = []
                   blob = x.lower().rstrip()                  
                   words += blob.split(" ")
                   
                   if(i == 0):
                       documents.append((list(words),'fr'))
                   elif(i == 1):
                       documents.append((list(words),'pt'))
                   elif(i == 2):
                       documents.append((list(words),'en'))
     return documents

          

def gettingAllWords(direcSelected):
     words = []
         
     for i in range(len(direcSelected)):

          direc = direcSelected[i]
          files = os.listdir(direc)
              
          sentences = [direc + sentence for sentence in files]

          
          for sentence in sentences:
               f = open(sentence, encoding="utf-8")
               blob = f.read().lower()
               
               words += blob.split(" ")

          print("len words: ",len(words))
          
          
     return words


def find_features(document):
     words = set(document)
     features = {}
     for w in word_features:
          features[w] = (w in words)

     return features


print("Generating documents...")

documents = generateDocuments(["samplefr/","sample/","sampleen/"])

    
save_documents = open("documentsFinalVersion.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()

print("Documents saved as documentsFinalVersion.pickle")


#documents_f = open("documentsFinalVersion.pickle","rb")
#documents = pickle.load(documents_f)
#documents_f.close()

random.shuffle(documents)



print("Generating all words...")
all_words = test(["samplefr/","sample/","sampleen/"])

save_allWords = open("allWordsFinalVersion.pickle","wb")
pickle.dump(all_words, save_allWords)
save_allWords.close()

#all_words_f = open("allWordsFinalVersion.pickle","rb")
#all_words = pickle.load(all_words_f)
#all_words_f.close()

print("Calculating the frequency distribution...")
all_words = nltk.FreqDist(all_words)

print("Showing the 50 most common words between all the words presented: ")
print(all_words.most_common(50))



print("Generating word_features...")
word_features = list(all_words.keys())[:5000]



print("Generating featuresets...")
featuresets = [(find_features(rev), category) for (rev, category) in documents]
#print(featuresets)

    
save_featureSets = open("featureSetsFinalVersion.pickle","wb")
pickle.dump(featuresets, save_featureSets)
save_featureSets.close()

#featuresets_f = open("featureSetsFinalVersion.pickle","rb")
#featuresets = pickle.load(featuresets_f)
#featuresets_f.close()

random.shuffle(featuresets)

print("Generating training set...")     
training_set = featuresets[7500:]

save_trainingSet = open("trainingSetFinalVersion.pickle","wb")
pickle.dump(training_set, save_trainingSet)
save_trainingSet.close()


#traning_set_f = open("trainingSetFinalVersion.pickle","rb")
#traning_set = pickle.load(traning_set_f)
#traning_set_f.close()



print("Generating testing set...")
testing_set =  featuresets[7500:10000]


save_testingSet = open("testingSetFinalVersion.pickle","wb")
pickle.dump(testing_set, save_testingSet)
save_testingSet.close()

#testing_set_f = open("testingSetFinalVersion.pickle","rb")
#testing_set = pickle.load(testing_set_f)
#testing_set_f.close()

print("Generating classifier...")
classifier = nltk.NaiveBayesClassifier.train(training_set)

save_classifier = open("classifierFinalVersion.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

#classifier_f = open("naivebayes4.pickle","rb")
#classifier = pickle.load(classifier_f)
#classifier_f.close()


def word_feats(words):
    return dict([(word, True) for word in words.split()])

while True:
     text = input("Type something: ").lower()
     print(classifier.classify(word_feats(text)))

print("Naive Bayes accuracy: ", (nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)



