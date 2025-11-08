from nltk.util import ngrams
n = 2 # you can give any number
sentence = 'You will face many defeats in life, but never let yourself be defeated.'
unigrams = ngrams(sentence.split(), n)
for item in unigrams:
    print(item)