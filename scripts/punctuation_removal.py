#import statements
import os
import string


#load text
dir = os.path.dirname(__file__)
filename = os.path.join(dir,'..','data', 'metamorphosis_clean.txt')
file_handle = open(filename, 'rt')
text = file_handle.read()
file_handle.close()

#splits the text into words by white space
words = text.split() #default delimiter : space
#print(words[:100])

#remove punctuation from each word
mapping_table = str.maketrans('', '', string.punctuation)
stripped_words = [w.translate(mapping_table) for w in words]
#print(stripped_words[:100])