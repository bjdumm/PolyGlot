#Run this to reset sections 

import pickle

categories = {"Nouns":"Nouns.txt","Adjectives":"Adjectives.txt","Verbs":"Verbs.txt","Other":"Other.txt"}
with open("sections.txt","wb") as fd:
    pickle.dump(categories,fd)
    

with open("sections.txt","rb") as fd:
    test = pickle.load(fd)
