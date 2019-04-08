# language-detection-machine-learning
Language detector built from scratch to recognize french, english and portuguese.


## About

That was my first Machine Learning project, It was not easy to do. I had to learn a lot of new concepts about Natural Language Processing and Deep Learning. I really loved to create this project because I also learned about a few classification algorithms (between them the Naive Bayes) and was a cool experience.


## Projects created with this algorithm

![My version of Google Tradutor Language Detection.](https://github.com/luaenrique/language-detection-machine-learning/tree/master/GoogleTradutorProject)



## How it works?

I've created this project using nltk (a python platform) with the Naive Bayes Algorithm.

To generate my dataset I've create two different robots with node.js, the first one collects articles from wikipedia based on a specific language and the another one organize those articles in different files and folders.

My dataset contains approximately 40.000 sentences per language.

## What is the Naive Bayes Algorithm?

When applied to Machine Learning, Naive Bayes Algorithm can be considered a probabilistic algorithm that considers each one of the features are independent. It is good for text classification because the probability of occurence of a word is not dependent of another word. 

## Next Steps

I am looking for ways to improve that algorithm the better as possible. I have read about Stemming and Lemmatization and I will probably apply those concepts to a new version of this project.
