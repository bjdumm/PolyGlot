#Run this to reset sections 

import pickle

categories = {"Nouns":"Nouns.txt","Adjectives":"Adjectives.txt","Verbs":"Verbs.txt"}
with open("sections.txt","wb") as fd:
    pickle.dump(categories,fd)
    