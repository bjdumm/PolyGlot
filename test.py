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


num = loadPickle("./Sections/numLangs.txt")
print(num)

words = loadPickle("./Sections/words.txt")
for k in words:
    words[k]["Spanish"] = ""
    words[k]["Italian"] = ""
    words[k]["French"] = ""
    words[k]["Greek"] = ""
    words[k]["Latin"] = ""
    words[k]["Russian"] = ""
    words[k]["Hebrew"] = ""
    words[k]["Japanese"] = ""
dumpPickle("./Sections/words.txt", words)





