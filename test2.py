from utils import loadPickle
import googletrans as gt

from utils import *
import wx

#Delete a language from words
words = loadPickle("words.txt")
#for k in list(words.keys()):
#    words[k].pop("Turkish",None)
#dumpPickle("words.txt",words)



d = {
    'Run': {'German': 'Laufen','Spanish':'Correr','Italian':'Buono','French':'Bon','Latin':''},
    'Eat': {'German': 'Essen','Spanish':'Comer','Italian':'Mangiare','French':'','Latin':''},
    'Jump': {'German': 'springen','Spanish':'saltar','Italian':'saltare','French':'big','Latin':''},
    'Know (Be familiar)': {'German': 'Wissen','Spanish':'conocer','Italian':'smallo','French':'small','Latin':''}
}

other = dumpPickle("Basic-Phrases.txt",d)

#dumpPickle("Basic-Phrases.txt",other)

