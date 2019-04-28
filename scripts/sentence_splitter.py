import os
from nltk import sent_tokenize

#load data
file_dir = os.path.dirname(__file__)
filename = os.path.join(file_dir, '..', 'data', 'metamorphosis_clean.txt')
file_handle = open(filename, 'rt')
text = file_handle.read()
file_handle.close()

#split the text into sentences using nltk's sentence tokenizer
sentences = sent_tokenize(text)
print(sentences[0])