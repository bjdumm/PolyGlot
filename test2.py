from utils import loadPickle
import googletrans as gt
import time

from utils import *
import wx

#Languages Greek = el, Russian = ru, latin = "La", hindi = "hi", mandarin="zh-CN", arabic="ar", hebrew="iw"

#Delete a language from words

verbs = loadPickle("Verbs.txt")
#for k in list(words.keys()):
#    words[k].pop("Turkish",None)
#dumpPickle("words.txt",words)



# 1 min = 300 words
#ani = loadPickle("Adjectives.txt")

#start = time.time()
#for k in list(ani.keys()):
    
    #ani[k]["German"] = gt.Translator().translate(k, dest="de").text
    #ani[k]["Spanish"] = gt.Translator().translate(k, dest="es").text
    #ani[k]["Italian"] = gt.Translator().translate(k, dest="it").text
    #ani[k]["French"] = gt.Translator().translate(k, dest="fr").text
    #ani[k]["Latin"] = gt.Translator().translate(k, dest="la").text
    #ani[k]["Greek"] = gt.Translator().translate(k, dest="el").text
    #ani[k]["Russian"] = gt.Translator().translate(k, dest="ru").text
    
    
#dumpPickle("Adjectives.txt", ani)

#print((time.time() - start))




#dumpPickle("Basic-Phrases.txt",other)
