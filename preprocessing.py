# ---------------------------- Import libraries--------------------------------------#
import string
# NLTK
import nltkmodules
import nltk
# NLTK Stopwords
from nltk.corpus import stopwords
# NLTK word tokenization
from nltk.tokenize import word_tokenize
# NLTK arabic stemmer
from nltk.stem.isri import ISRIStemmer
# Regular expression
import re


# Modify stopword list
# Define stop_words list
stop_words = stopwords.words('arabic') 
# Create new list
stop_words1 = [] 
# Iterate through the stopwords list
for word in stop_words:

    stop_words1.append('و'+word) # Add 'و' to the stopword and append it to the stopwords1 list
    stop_words1.append('ب'+word) # Add 'ب' to the stopword and append it to the stopwords1 list
    stop_words1.append('ف'+word) # Add 'ف' to the stopword and append it to the stopwords1 list
    stop_words1.append(word+'ه') # Add 'ه' to the stopword and append it to the stopwords1 list
    stop_words1.append(word+'ها') # Add 'ها' to the stopword and append it to the stopwords1 list

# Merge the modified stop words with original stop words list
stop_words = stop_words1+stop_words 
# Append 'قبل' to the stopwords1 list 
stop_words.append('قبل') 
# Append 'و' to the stopwords1 list
stop_words.append("و")  

# ---------------------- Preprocessing function ------------------------------#

def data_preprocessing(article):
     
    article = re.sub('\n',' ',article) # Removing this character
    article = re.sub('الـ','',article) # Removing this character
    article = re.sub('لـ','',article) # Removing this character
    article = re.sub('بـ','',article) # Removing this character
    article = re.sub('ال','',article) # Removing this character
    article = re.sub('عربية نت ','',article) # Removing this sentence
    
    # Spilt the keyword name by comma 
    tokens = word_tokenize(str(article)) 
    # Define a list of punctuation
    remove_pun = str.maketrans('', '', string.punctuation) 
    # Remove punctuation from each word 
    words = [w.translate (remove_pun) for w in tokens ]
    # Remove non-alphabetic characters 
    alphabetic_words = [word for word in words if word.isalpha()]
    # Remove arabic stopwords 
    alphabetic_words = [word for word in alphabetic_words if not word in stop_words ]
    # Initialize arabic stemmer
    stemer = ISRIStemmer() 
    # Stem each word 
    stemmed_words = [stemer.suf32(word) for word in alphabetic_words ] 
    # Join and return the stemmed_words
    return " ".join(stemmed_words)
