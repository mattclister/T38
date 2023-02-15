import spacy
nlp = spacy.load('en_core_web_md')

# Snippet 1

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Cat and monkey are most similar as the same type. "Animal"
# Banana and monkey are not similar but appear to be quite related. 
# Presumably because they are often assosiated.
# Banana and cat are the least related, as I would expect.

# Simpler language model

simple = spacy.load('en_core_web_sm')

word1 = simple("cat")
word2 = simple("monkey")
word3 = simple("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Doing this triggers a warning: 
# "The model you're using has no word vectors loaded, 
# so the result of the Doc.similarity method will be based on the tagger, 
# parser and NER, which may not give useful similarity judgements. 
# This may happen if you're using one of the small models, 
# e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
# You can always add your own word vectors, or use one of the larger models instead if available."