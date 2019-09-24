# Python program to generate word vectors using Word2Vec

# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action = 'ignore')

import gensim
from gensim.models import Word2Vec

 # Read in 'APWA Transcriptions' File
sample = open("APWATranscriptions-WC2.txt", "r")
s = sample.read()

# Replaces escape character with space
f = s.replace("\n", " ")

data = []

# iterate through each sentence in the file
for i in sent_tokenize(f):
    temp = []

    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower())

    data.append(temp)

# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count = 1,
                              size = 100, window = 5)

# Print results
print("Cosine similarity between 'prison' " +
               "and 'punishment' - CBOW : ",
    model1.similarity('prison', 'punishment'))

print("Cosine similarity between 'prison' " +
                 "and 'inmate' - CBOW : ",
      model1.similarity('prison', 'inmate'))

# Create Skip Gram model
model2 = gensim.models.Word2Vec(data, min_count = 1, size = 100,
                                             window = 5, sg = 1)

# Print results
print("Cosine similarity between 'prison' " +
          "and 'punishment' - Skip Gram : ",
    model2.similarity('prison', 'punishment'))

print("Cosine similarity between 'prison' " +
            "and 'inmate' - Skip Gram : ",
      model2.similarity('prison', 'inmate'))
