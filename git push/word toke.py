# Import required libraries
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
# Download necessary resources (run once)
nltk.download("punkt")
nltk.download("stopwords")
# Sample text
text = "Bharathi Education Trust polytechnic is giving good result in computer science department"
# 1. Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:", sentences)
# 2. Word Tokenization
words = word_tokenize(text)
print("\nWord Tokenization:", words)
# 3. Dropping Stop Words
stop_words = set(stopwords.words("english"))
filtered_words = [w for w in words if w.lower() not in stop_words]
print("\nWithout Stopwords:", filtered_words)
# 4. Dropping Punctuation
punct_removed = [w for w in filtered_words if w not in string.punctuation]
print("\nWithout Punctuation:", punct_removed)