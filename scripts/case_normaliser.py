import os

#load data
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..', 'data','metamorphosis_clean.txt')
file_handle = open(filename, 'rt')
text = file_handle.read()
file_handle.close()

#split words by whitespace
words = text.split()

#converting to lowercase
words = [word.lower() for word in words]
#print(words[:100])

#converting to UPPERCASE
words = [word.upper() for word in words]
#print(words[:100])