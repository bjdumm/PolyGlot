from utils import loadPickle
import googletrans as gt
import time

from utils import *
import wx

"""LANGUAGES = {
2 'af': 'afrikaans',
3 'sq': 'albanian',
4 'ar': 'arabic',
5 'be': 'belarusian',
6 'bg': 'bulgarian',
7 'ca': 'catalan',
8 'zh-CN': 'chinese_simplified',
9 'zh-TW': 'chinese_traditional',
10 'hr': 'croatian',
11 'cs': 'czech',
12 'da': 'danish',
13 'nl': 'dutch',
14 'en': 'english',
15 'eo': 'esperanto',
16 'et': 'estonian',
17 'tl': 'filipino',
18 'fi': 'finnish',
19 'fr': 'french',
20 'gl': 'galician',
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
33 'lv': 'latvian',
34 'lt': 'lithuanian',
35 'mk': 'macedonian',
36 'ms': 'malay',
37 'mt': 'maltese',
38 'no': 'norwegian',
39 'fa': 'persian',
40 'pl': 'polish',
41 'pt': 'portuguese',
42 'ro': 'romanian',
43 'ru': 'russian',
44 'sr': 'serbian',
45 'sk': 'slovak',
46 'sl': 'slovenian',
47 'es': 'spanish',
48 'sw': 'swahili',
49 'sv': 'swedish',
50 'th': 'thai',
51 'tr': 'turkish',
52 'uk': 'ukrainian',
53 'vi': 'vietnamese',
54 'cy': 'welsh',
55 'yi': 'yiddish',
56 }
"""

#Delete a language from words


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

others = loadPickle("sections.txt")
for k in others:
    others[k] = "./Sections/" + others[k]

print(others)
    
#dumpPickle("sections.txt", others)