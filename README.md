# Introductory studies in Natural Language Processing (NLP)

NLP is a very important field in the current usage of Machine Learning (ML). 
It is used to make a machine capable of make inferences and predictions related
to language. 

NLP uses the concept of word vector (embeddings) through the Word2Vec mecanism
to be able to do machine learning. So, this concept is implemented is the following
manner: one word is represented as a point (with n dimensions, n as a real number 
greater or equal to 1) in a vector space. So, each word has n numerical components (vector n-dimensional)
that depicts it's location in the vector space. 
Words that are next to each other are similar, synonim or related word. Words that are
far apart are dissimilar or not related. 

With the words in a document represented as vector (with can be also a set o parameters
to be learned in a neural network), we can use different models to explore the power
of NLP. For example, we have models such as: Continuous Bag of Words (CBOW), Skip-Gram, 
Long Short-Term Memory (LSTM) and Simple Word Embeddings Model (SWEM).

1. CBOW: Uses the words to predict another word in an environment, in such a way that 
the order of the words in the document is not relevant.
2. Skip-Gram: Similar to CBOW, but uses the word to predict the other words in the 
environment.
3. LSTM: More complicated model that is used to produce Text-Synthesis. Is based on
Recurrent Neural Networks (RNN), and uses the concepts of units and memory cells to 
be sucessful.
4. SWEM: Simple model that is used in majority to produce Sentiment Analysis. Uses
all the words in a document in such a way to produce a final vector that represents
the entire document (that can be done calculating the mean of all vector, for example).
This vector is sent through a simple perceptron with a simple classification, such as 
logistic regression.

This repository represents intro studies on the matter, with it's applications
in Python on different fields.