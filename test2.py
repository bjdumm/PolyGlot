from utils import loadPickle
import translate as gt
import time

from utils import *
import wx


"""
Portuguese
Hindi
Swedish
Dutch
Arabic
Japanese
Polishh
Romanian
Hungarian
Irish 
Chinese
Korean
Hebrew
Icelandic
Danish
Bengali
Afrikaans
serbian
"""





"""LANGUAGES = {
2 'af': 'afrikaans',
3 'sq': 'albanian',
4 'ar': 'arabic',
8 'zh-CN': 'chinese_simplified',
12 'da': 'danish',
13 'nl': 'dutch',
14 'en': 'english'
19 'fr': 'french',
21 'de': 'german',
22 'el': 'greek',
23 'iw': 'hebrew',
24 'hi': 'hindi',
25 'hu': 'hungarian',
26 'is': 'icelandic',
27 'id': 'indonesian',
28 'ga': 'irish',
29 'it': 'italian',
30 'ja': 'japanese',
'ko': 'korean',
32 'la': 'latin',
38 'no': 'norwegian',
40 'pl': 'polish',
41 'pt': 'portuguese',
42 'ro': 'romanian',
43 'ru': 'russian',
44 'sr': 'serbian',
45 'sk': 'slovak',
47 'es': 'spanish',
49 'sv': 'swedish',
"""

#Delete a language from words

verbs1 = loadPickle("./Sections/sections.txt")
verbs2= loadPickle("./Sections/nounSections.txt")
verbs3 = loadPickle("./Sections/verbSections.txt")

print(verbs1)
print(verbs2)
print(verbs3)
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
