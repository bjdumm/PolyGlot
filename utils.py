from json import load
import pickle
import os
import random 
import wx
import wx.grid

#Display words in dictionary in cells
#Pass the grid object and dictionary to be printed
def displayWords(grid, words):
    
    #words[list(words)[0]] -> {"German: '', "Spanish: '' .... "}
    #len(list(words)) -> how many english words there are (rows)
    #words[word][list(foreignDic)[col]] -> foreign word value at words[engWOrd][ForeignLanguage] for the col'th index in the language label array

    colRange = len(words[list(words)[0]]) + 1
    for row in range(len(list(words))):
        word = list(words)[row]
        grid.SetCellValue(row, 0, list(words)[row])
        grid.SetColLabelValue(0, 'English')
        for col in range(1,colRange):
            engWord = list(words)[0]
            foreignDic = words[engWord]  #THe foreign dic for engWord
            grid.SetCellValue(row,col, words[word][list(foreignDic)[col-1]])
    
    #Language Labels
    engWord = list(words)[0]  #Just grabs first english word (could be any one)
    for col in range(1,len(words[engWord])+1):  #Gets first english word dictionary
        grid.SetColLabelValue(col, list(words[engWord])[col-1])

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
def sortDic(dic):
    keys = sorted(dic)
    sortedDic = {}
    for k in keys:
        sortedDic[k] = dic[k]
    return sortedDic



def shuffleDic(dic):
    keys = list(dic.keys())
    random.shuffle(keys)
    shuffledDic = {}
    for k in keys:
        shuffledDic[k] = dic[k]
    return shuffledDic

