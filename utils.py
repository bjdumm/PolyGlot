from json import load
import pickle
import os
import wx
import wx.grid

#Display words in dictionary in cells
#Pass the grid object and dictionary to be printed
def displayWords(grid, words):
    numLangs = loadPickle("numLangs.txt")
    for row in range(len(list(words))):
        word = list(words)[row]
        grid.SetCellValue(row, numLangs, list(words)[row])
        grid.SetColLabelValue(numLangs, 'English')
        for col in range(len(words[list(words)[0]])):
            engWord = list(words)[0]
            foreignWord = words[engWord]
            grid.SetCellValue(row,col, words[word][list(foreignWord)[col]])
    
    engWord = list(words)[0]
    for col in range(len(words[list(words)[0]])):
        grid.SetColLabelValue(col, list(words[engWord])[col])

#Function to load a pickled dictionary and return it
def loadPickle(file):
    """Takes file name, Returns a dictionary"""
    
    if (os.path.exists(file)):
        with open(file,"rb") as fd:
            data = pickle.load(fd)
    else:
        return False
    return data

#Number of languages currently in saved data
#numLangs = loadPickle("numLangs.txt")


#Function to pickle python dictionary and save it
def dumpPickle(file,data):
    """Takes a file name and a dictionary -> return Bool"""
    with open(file,"wb") as fd:
        pickle.dump(data,fd)
    return True


def getLanguageName(lang):
    return "Garbage"



def delLanguage(lang):
    nounSections = loadPickle("nounSections.txt")
    otherSections = loadPickle("otherSections.txt")
    adverbSections = loadPickle("adverbSections.txt")
    adjSections = loadPickle("adjSections.txt")
    verbSections = loadPickle("verbSections.txt")
    sections = loadPickle("sections.txt")

    data = loadPickle("words.txt")
    for k in list(data.keys()):
        data[k].pop(lang,None)
    dumpPickle("words.txt",data)

    for sec in sections:
        dic = loadPickle(f"{sections[sec]}")
        for k in list(dic.keys()):
            dic[k].pop(lang,None)
        dumpPickle(f"{sections[sec]}", dic)

    for sec in verbSections:
        dic = loadPickle(f"{verbSections[sec]}")
        for k in list(dic.keys()):
            dic[k].pop(lang,None)
        dumpPickle(f"{verbSections[sec]}", dic)

    for sec in adjSections:
        dic = loadPickle(f"{adjSections[sec]}")
        for k in list(dic.keys()):
            dic[k].pop(lang,None)
        dumpPickle(f"{adjSections[sec]}", dic)

    for sec in adverbSections:
        dic = loadPickle(f"{adverbSections[sec]}")
        for k in list(dic.keys()):
            dic[k].pop(lang,None)
        dumpPickle(f"{adverbSections[sec]}", dic)
    
    for sec in otherSections:
        dic = loadPickle(f"{otherSections[sec]}")
        for k in list(dic.keys()):
            dic[k].pop(lang,None)
        dumpPickle(f"{otherSections[sec]}", dic)
    
    for sec in nounSections:
        dic = loadPickle(f"{nounSections[sec]}")
        for k in list(dic.keys()):
            dic[k].pop(lang,None)
        dumpPickle(f"{nounSections[sec]}", dic)


def addLanguage(newLang):
    nounSections = loadPickle("nounSections.txt")
    otherSections = loadPickle("otherSections.txt")
    adverbSections = loadPickle("adverbSections.txt")
    adjSections = loadPickle("adjSections.txt")
    verbSections = loadPickle("verbSections.txt")
    sections = loadPickle("sections.txt")

    words = loadPickle("words.txt")
    for k in words:
        words[k][newLang] = ""
    dumpPickle("words.txt",words)

    #Load section -> Add lang : "" -> dump to txt file
    for sec in sections:
        dic = loadPickle(f"{sections[sec]}")
        for k in dic:
            dic[k][newLang] = ""
        dumpPickle(f"{sections[sec]}", dic)
    
    for sec in verbSections:
        dic = loadPickle(f"{verbSections[sec]}")
        for k in dic:
            dic[k][newLang] = ""
        dumpPickle(f"{verbSections[sec]}",  dic)

    for sec in adjSections:
        dic = loadPickle(f"{adjSections[sec]}")
        for k in dic:
            dic[k][newLang] = ""
        dumpPickle(f"{adjSections[sec]}",  dic)

    for sec in adverbSections:
        dic = loadPickle(f"{adverbSections[sec]}")
        for k in dic:
            dic[k][newLang] = ""
        dumpPickle(f"{adverbSections[sec]}", dic)
    
    for sec in otherSections:
        dic = loadPickle(f"{otherSections[sec]}")
        for k in dic:
            dic[k][newLang] = ""
        dumpPickle(f"{otherSections[sec]}", dic)
    
    for sec in nounSections:
        dic = loadPickle(f"{nounSections[sec]}")
        for k in dic:
            dic[k][newLang] = ""
        dumpPickle(f"{nounSections[sec]}", dic)
    
    return



#Alphabetizes a dictionary
def sortDic(data):
    return sorted(data)
def deleteSection():
    pass
def addFile():
    pass


"""
def renderSection(grid, section):
    nounSections = loadPickle("nounSections.txt")
    adverbSections = loadPickle("adverbSections.txt")
    adjectiveSections = loadPickle("adjSections.txt")
    verbSections = loadPickle("verbSections.txt")
    otherSections = loadPickle("otherSections.txt")

    if (os.path.exists(f"{section}.txt")):
        data = loadPickle(f"{section}.txt")
    elif (section in nounSections):
        data = loadPickle(nounSections[section])
    elif (section in adverbSections):
        data = loadPickle(f"{section}.txt")
    elif (section in adjectiveSections):
        data = loadPickle(f"{section}.txt")
    elif (section in verbSections):
        data = loadPickle(f"{verbSections[section]}")
    elif (section in otherSections):
        data = loadPickle(f"{otherSections[section]}")
    else:
        print("Section was not found.")
    
    displayWords(grid, data)

    return
"""