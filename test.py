import translate
import os
from utils import loadPickle,dumpPickle
import time
import wx

#Manually set numLangs to the second value
#dumpPickle("numLangs.txt",5)
#num = loadPickle("numLangs.txt")
#print("The current number of languages is set at : ", num)

#Check current Sections:


#print("The     current sections are " , secs)

#Check current Adverb Sections
#adv = loadPickle("adverbSections.txt")
#print("The current adverb sections are: ", adv)

#Check current Noun Sections
#nSec = loadPickle("nounSections.txt")
#print("The current noun sections are: ", nSec)


#sections = loadPickle("sections.txt")
#for sec in sections:
#    dic = loadPickle(f"{sections[sec]}")
#    print(dic)


#for eng in nouns:
#   nouns[eng]['Latin'] = ""
#dumpPickle("Nouns.txt", nouns)



#sections = loadPickle("sections.txt")
##for sec in sections:
#    dic = loadPickle(f"{sections[sec]}")
#    for k in dic:
#        dic[k]["Mandarin"] = ""
#    print(f"Thsi is the data for {sections[sec]}\n\n")
#    print(dic)




def removeBlank(lang1, file):
    secs = loadPickle(file)
    for s in secs:
        try:
            secs[s].pop(lang1)
        except:
            continue
       # secs[s].pop(lang2)
    print(secs)
    dumpPickle(file, secs)
    print("Successo")


removeBlank("Chinese", "./Sections/Future.txt")



def checkFile(file):
    f = loadPickle(file)
    print(f)

#checkFile("./Sections/Future.txt")
