import os
from nltk.tokenize import word_tokenize

#load data from file
file_dir = os.path.dirname(__file__)
filename = os.path.join(file_dir, '..', 'data', 'metamorphosis_clean.txt')
file_handle = open(filename)
text = file_handle.read()
file_handle.close()

# NLTK provides a function called word_tokenize() for splitting strings into tokens,
# It splits tokens based on white space and punctuation
# 

tokens = word_tokenize(text)
print(tokens[:100])
