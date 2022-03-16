import pickle
import os
import wx
import wx.grid

#Display words in dictionary in cells
#Pass the grid object and dictionary to be printed
def displayWords(grid, words):
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
numLangs = loadPickle("numLangs.txt")


#Function to pickle python dictionary and save it
def dumpPickle(file,data):
    """Takes a file name and a dictionary -> return Bool"""
    with open(file,"wb") as fd:
        pickle.dump(data,fd)
    return True


def getLanguageAbbrev(lang):
    initials = {'french':'fr','german':'de','spanish':'es','italian':'it','russian':'ru','latin':'la','greek':'gk'}
    lang = lang.tolower()
    return initials[lang]

def getLanguageName(lang):
    return "Garbage"




    
def delLanguage(data,lang):
    for k in list(data.keys()):
        data[k].pop(lang,None)
    return data










#Alphabetizes a dictionary
def sortDic(data):
    return sorted(data)

def deleteSection():
    pass

def addLanguage():
    pass


def addFile():
    pass
