import pickle 

#English dictionary
#Key is english word, then the key of that gives the 
#word in the specified language:
#E.x.  eng['Hello']['German] = 'Hallo'

vocab = {
    
    'Hello': {'German': 'Hallo', 'Spanish': 'Hola', 'Italian': 'Ciao', 'French' : 'Fr', 'Latin': 'elli', 'DeleteMe': ''}, 
    'Goodbye': {'German': 'Auf Wiedersehen', 'Spanish': 'Adios', 'Italian': 'Ciao', 'French':'Fr','Latin': 'govni', 'DeleteMe': ''},
    'Boy': {'German': 'Der Junge', 'Spanish': 'el nino', 'Italian': 'il boyi', 'French':'Fr', 'Latin': 'sumni', 'DeleteMe': ''},
    'To Eat': {'German': 'Essen', 'Spanish': 'comer', 'Italian': 'mangiare', 'French':'Fr', 'Latin': 'eatere', 'DeleteMe': ''},
    'Good': {'German': 'Gut', 'Spanish': 'Bueno', 'Italian': 'Buono', 'French':'Fr', 'Latin': 'bene', 'DeleteMe': ''},
    'Bad': {'German': 'Schlimm/Schlecht', 'Spanish': 'mal', 'Italian': 'Ciao', 'French':'Fr', 'Latin': 'ello', 'DeleteMe': ''},
    'Big': {'German': 'Gross', 'Spanish': 'grande', 'Italian': 'big', 'French':'Fr', 'Latin': 'does', 'DeleteMe': ''}, 
    'Small': {'German': 'klein', 'Spanish': 'poco', 'Italian': 'smallo', 'French':'Fr', 'Latin': 'this', 'DeleteMe': ''},
    'Dog': {'German': 'der Hund', 'Spanish': 'el perro', 'Italian': 'Buono', 'French':'Fr', 'Latin': 'work', 'DeleteMe': ''},
    'Cat': {'German': 'die Katze', 'Spanish': 'el gato', 'Italian': 'Ciao', 'French':'Fr', 'Latin': 'now?', 'DeleteMe': ''},
    'Bat': {'German': 'Fliedermaus', 'Spanish': 'grande', 'Italian': 'big', 'French':'Fr', 'Latin': '', 'DeleteMe': ''},
    'Elephant': {'German': '', 'Spanish': 'el elefante', 'Italian': 'smallo', 'French':'Fr', 'Latin': '', 'DeleteMe': ''},
}

adjectives = {
    'Good': {'German': 'Gut','Spanish':'Bueno','Italian':'Buono','French':'Bon'},
    'Bad': {'German': 'Schlimm/Schlecht','Spanish':'mal','Italian':'Ciao','French':'bado'},
    'Big': {'German': 'Gross','Spanish':'grande','Italian':'big','French':'big'},
    'Small': {'German': 'klein','Spanish':'poco','Italian':'smallo','French':'small'}
}

nouns = {
    'Dog': {'German': 'der Hund','Spanish':'el perro','Italian':'Buono','French':'Bon'},
    'Cat': {'German': 'die Katze','Spanish':'el gato','Italian':'Ciao','French':'bado'},
    'Bat': {'German': 'Fliedermaus','Spanish':'grande','Italian':'big','French':'big'},
    'Elephant': {'German': '','Spanish':'el elefante','Italian':'smallo','French':'small'}
}

verbs = {
    'Run': {'German': 'Laufen','Spanish':'Correr','Italian':'Buono','French':'Bon','Latin':''},
    'Eat': {'German': 'Essen','Spanish':'Comer','Italian':'Mangiare','French':'','Latin':''},
    'Jump': {'German': 'springen','Spanish':'saltar','Italian':'saltare','French':'big','Latin':''},
    'Know (Be familiar)': {'German': 'Wissen','Spanish':'conocer','Italian':'smallo','French':'small','Latin':''}
}

adverbs = {
    'Run': {'German': 'Laufen','Spanish':'Correr','Italian':'Buono','French':'Bon'},
    'Eat': {'German': 'Essen','Spanish':'Comer','Italian':'Mangiare','French':''},
    'Jump': {'German': 'springen','Spanish':'saltar','Italian':'saltare','French':'big'},
    'Know (Be familiar)': {'German': 'Wissen','Spanish':'conocer','Italian':'smallo','French':'small'}
}

preps = {
    'Run': {'German': 'Laufen','Spanish':'Correr','Italian':'Buono','French':'Bon'},
    'Eat': {'German': 'Essen','Spanish':'Comer','Italian':'Mangiare','French':''},
    'Jump': {'German': 'springen','Spanish':'saltar','Italian':'saltare','French':'big'},
    'Know (Be familiar)': {'German': 'Wissen','Spanish':'conocer','Italian':'smallo','French':'small'}
}

other = {
    'Run': {'German': 'Laufen','Spanish':'Correr','Italian':'Buono','French':'Bon'},
    'Eat': {'German': 'Essen','Spanish':'Comer','Italian':'Mangiare','French':''},
    'Jump': {'German': 'springen','Spanish':'saltar','Italian':'saltare','French':'big'},
    'Know (Be familiar)': {'German': 'Wissen','Spanish':'conocer','Italian':'smallo','French':'small'}
}




#Use this to manually reset words dictionary
#with open("words.txt" , "rb") as fd:
#    v = pickle.load(fd)
#    print(v)

#fd3 = open("Verbs.txt","wb")
#pickle.dump(verbs, fd3)

#fd3 = open("Adjectives.txt","wb")
#pickle.dump(adjectives, fd3)

#with open("Adverbs.txt","wb") as fd:
    #pickle.dump(adverbs, fd)

#with open("Adverbs.txt","rb") as fd:
#    dic = pickle.load(fd)
#print(dic)

#with open("Prepositions.txt","wb") as fd:
#    dic = {
#        'On': {'German': 'Auf','Spanish':'en','Italian':'','French':'Bon','Latin':'inni'}
#    }
#    pickle.dump(dic, fd)

#with open("Other.txt","wb") as fd:
#    dic = {
#        'Other': {'German': 'Andere','Spanish':'otro','Italian':'','French':'?','Latin':'inni'}
#    }
#    pickle.dump(dic, fd)

#with open("Verbs.txt","wb") as fd:
#    pickle.dump(verbs,fd)
    
#print(dic)

#with open("Other.txt","rb") as fd:
#    dic = pickle.load(fd)
#print(dic)
