import os
from nltk.tokenize import word_tokenize

#load data from file
file_dir = os.path.dirname(__file__)
filename = os.path.join(file_dir, '..', 'data', 'metamorphosis_clean.txt')
file_handle = open(filename)
text = file_handle.read()
file_handle.close()

#split text into tokens
tokens = word_tokenize(text)

#remove all tokens that are not alphabetic
#str.isalpha() - Return true if all characters in the string are alphabetic and there is at least one character, false otherwise. 
words = [word for word in tokens if word.isalpha()] 
print(words[:100])