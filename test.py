import googletrans
import os
from utils import loadPickle,dumpPickle

#Manually set numLangs to the second value
#dumpPickle("numLangs.txt",5)
num = loadPickle("numLangs.txt")
#print("The current number of languages is set at : ", num)

#Check current Sections:
secs = loadPickle("sections.txt")
#print("The current sections are " , secs)

#Check current Adverb Sections
adv = loadPickle("adverbSections.txt")
#print("The current adverb sections are: ", adv)

#Check current Noun Sections
nSec = loadPickle("nounSections.txt")
#print("The current noun sections are: ", nSec)


#sections = loadPickle("sections.txt")
#for sec in sections:
#    dic = loadPickle(f"{sections[sec]}")
#    print(dic)

nouns = loadPickle("Nouns.txt")
#for eng in nouns:
#   nouns[eng]['Latin'] = ""
#dumpPickle("Nouns.txt", nouns)
print(nouns)


#sections = loadPickle("sections.txt")
##for sec in sections:
#    dic = loadPickle(f"{sections[sec]}")
#    for k in dic:
#        dic[k]["Mandarin"] = ""
#    print(f"Thsi is the data for {sections[sec]}\n\n")
#    print(dic)








