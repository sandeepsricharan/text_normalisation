import os
import string
from nltk.corpus import stopwords


#load data from file
file_dir = os.path.dirname(__file__)
filename = os.path.join(file_dir, '..', 'data', 'metamorphosis_clean.txt')
file_handle = open(filename)
text = file_handle.read()
file_handle.close()

#load all english stopwords
stop_words = stopwords.words('english')
#print(stop_words)

# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

# convert to lower case
tokens = [w.lower() for w in tokens]

# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

# filter out stop words
words = [w for w in words if not w in stop_words]
print(words[:100])