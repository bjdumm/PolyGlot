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



fd = open("words.txt" , "rb")
vocab = pickle.load(fd)

#fd2 = open("nouns.txt","rb")
#nouns = pickle.load(fd2)

#fd3 = open("verbs.txt","rb")
#nouns = pickle.load(fd3)



#Ideas:
#Add option to color specific row to make it pop more
#Add ability to add a language and column -> increment numLangs inject new column with that label
#Add some buttons for extra features



#len(list(dic)) -> Number of rows
#len(list(dic)[0]) -> Number of cols