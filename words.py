import pickle 

#English dictionary
#Key is english word, then the key of that gives the 
#word in the specified language:
#E.x.  eng['Hello']['German] = 'Hallo'

vocab = {
    'Hello': {'German': 'Hallo','Spanish':'Hola','Italian':'Ciao','French':'Bonjour'},
    'Goodbye': {'German': 'Auf Wiedersehen','Spanish':'Adios','Italian':'Ciao','French':'Au Revoir'},
    'Boy': {'German': 'Der Junge','Spanish':'el nino','Italian':'il boyi','French':'le garcon'},
    'To Eat': {'German': 'Essen','Spanish':'comer','Italian':'mangiare','French':'mangiare'},
    'Good': {'German': 'Gut','Spanish':'Bueno','Italian':'Buono','French':'Bon'},
    'Bad': {'German': 'Schlimm/Schlecht','Spanish':'mal','Italian':'Ciao','French':'bado'},
    'Big': {'German': 'Gross','Spanish':'grande','Italian':'big','French':'big'},
    'Small': {'German': 'klein','Spanish':'poco','Italian':'smallo','French':'small'},
    'Dog': {'German': 'der Hund','Spanish':'el perro','Italian':'Buono','French':'Bon'},
    'Cat': {'German': 'die Katze','Spanish':'el gato','Italian':'Ciao','French':'bado'},
    'Bat': {'German': 'Fliedermaus','Spanish':'grande','Italian':'big','French':'big'},
    'Elephant': {'German': '','Spanish':'el elefante','Italian':'smallo','French':'small'}
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
    'Run': {'German': 'Laufen','Spanish':'Correr','Italian':'Buono','French':'Bon'},
    'Eat': {'German': 'Essen','Spanish':'Comer','Italian':'Mangiare','French':''},
    'Jump': {'German': 'springen','Spanish':'saltar','Italian':'saltare','French':'big'},
    'Know (Be familiar)': {'German': 'Wissen','Spanish':'conocer','Italian':'smallo','French':'small'}
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



#fd = open("words.txt" , "rb")
#vocab = pickle.load(fd)

#fd2 = open("Nouns.txt","wb")
#pickle.dump(nouns, fd2)

#fd3 = open("Verbs.txt","wb")
#pickle.dump(verbs, fd3)

#fd3 = open("Adjectives.txt","wb")
#pickle.dump(adjectives, fd3)

#with open("Adverbs.txt","wb") as fd:
    #pickle.dump(adverbs, fd)

with open("Adverbs.txt","rb") as fd:
    dic = pickle.load(fd)
#print(dic)

#len(list(dic)) -> Number of rows
#len(list(dic)[0]) -> Number of cols