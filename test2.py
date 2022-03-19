from utils import loadPickle
import googletrans as gt

from utils import *
import wx

#Delete a language from words
words = loadPickle("words.txt")
#for k in list(words.keys()):
#    words[k].pop("Turkish",None)
#dumpPickle("words.txt",words)


print(words)


other = loadPickle("Basic-Phrases.txt")
print(other)

#dumpPickle("Basic-Phrases.txt",other)

