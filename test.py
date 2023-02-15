import spacy
nlp = spacy.load('en_core_web_md')
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