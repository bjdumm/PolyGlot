from ast import dump
from wx.core import DF_BITMAP, GREEN, YES_NO
import wx
import wx.grid
import os
import pickle
import googletrans as gt
#from utils import loadPickle, dumpPickle, displayWords, numLangs, getLanguageAbbrev, getLanguageName
from utils import *

class ShowButton:
    def __init__(self, parent, lbl, sz, ps):
        btn = wx.Button(parent, label=lbl, size=sz, pos=ps)
        btn.Bind(wx.EVT_BUTTON, TestFrame.showHide)


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="PolyGlot",
                          size=(640,480)) 
        
        #Global Variables for Entire Frame
        self.numLangs = loadPickle("numLangs.txt")
        self.rootIdx = 2
        self.vocabIdx = 2
        self.currentGrid = "words"
        self.nounList = loadPickle("nounSections.txt")
        self.adjectiveList = loadPickle("adjSections.txt")
        self.adverbList = loadPickle("adverbSections.txt")
        self.verbList = loadPickle("verbSections.txt")
        self.otherList = loadPickle("otherSections.txt") 
        self.sections = loadPickle("sections.txt")

        #Left Hand Tree
        self.treePanel = wx.Panel(self, size=wx.Size(250,1800), pos= wx.Point(0,0))
        self.tree = wx.TreeCtrl(self.treePanel,size=wx.Size(150,3000))
        root = self.tree.AddRoot("Polyglot")  

        self.adjectives = self.tree.InsertItem(root,0,"Adjectives")
        for idx, k in enumerate(self.adjectiveList):
            self.tree.InsertItem(self.adjectives,idx,k)

        self.nouns = self.tree.InsertItem(root,1,"Nouns")
        for idx, k in enumerate(self.nounList):
            self.tree.InsertItem(self.nouns,idx,k)
            
        self.verbs = self.tree.InsertItem(root,2,"Verbs")  #Verbs Section
        for idx, k in enumerate(self.verbList):
            self.tree.InsertItem(self.verbs,idx,k)
        
        self.vocab = self.tree.InsertItem(root,3,"words")   
        
        self.adverbs = self.tree.InsertItem(root,4,"Adverbs")
        for idx, k in enumerate(self.adverbList):
            self.tree.InsertItem(self.adverbs,idx,k)

        self.preps = self.tree.InsertItem(root,5,"Prepositions")
       
        self.other = self.tree.InsertItem(root,6,"Other")
        for idx, k in enumerate(self.otherList):
            self.tree.InsertItem(self.other,idx,k)

        self.tree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.ChangeContent)
        
        #Center Grid
        self.gridPanel = wx.Panel(self, size=wx.Size(1000,1000), pos=wx.Point(150,0))
        self.grid = wx.grid.Grid(self.gridPanel,size=wx.Size(1000,1000))
        self.grid.CreateGrid(1000 ,self.numLangs + 3)
        self.grid.SetDefaultCellBackgroundColour(wx.Colour(255,255,255))
        self.grid.SetDefaultCellOverflow(False)
        self.grid.SetDefaultCellFont(wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_MEDIUM))
        self.grid.EnableGridLines(True)
        dic = loadPickle("words.txt")
        displayWords(self.grid, dic)
        self.grid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.OnChangeCell)

        #Language Panel RHS
        self.langPanel = wx.Panel(self,pos=wx.Point(1200,0),size=wx.Size(750,500))
        self.enterNoun = wx.TextCtrl(self.langPanel, -1,"", wx.Point(175,15))
        self.enterNoun.SetInsertionPoint(0)
        self.enterVerb = wx.TextCtrl(self.langPanel, -1,"", wx.Point(175,40))
        self.enterVerb.SetInsertionPoint(0)
        self.enterAdj = wx.TextCtrl(self.langPanel, -1,"", wx.Point(175,65))
        self.enterAdj.SetInsertionPoint(0)
        self.enterAdverb = wx.TextCtrl(self.langPanel, -1,"", wx.Point(175,90))
        self.enterAdverb.SetInsertionPoint(0)
        self.enterOther = wx.TextCtrl(self.langPanel, -1,"", wx.Point(175,115))
        self.enterOther.SetInsertionPoint(0)
        nounBtn = wx.Button(self.langPanel, label="Add Noun Category: ", size=wx.Size(135,23), pos=wx.Point(25,15))
        verbBtn = wx.Button(self.langPanel, label="Add Verb Category: ", size=wx.Size(135,23), pos=wx.Point(25,40))
        adjBtn = wx.Button(self.langPanel, label="Add Adjective Category: ", size=wx.Size(135,23), pos=wx.Point(25,65))
        adverbBtn = wx.Button(self.langPanel, label="Add Adverb Category: ", size=wx.Size(135,23), pos=wx.Point(25,90))
        otherBtn = wx.Button(self.langPanel, label="Add Other Category: ", size=wx.Size(135,23), pos=wx.Point(25,115))
        otherBtn.Bind(wx.EVT_BUTTON, self.addOther)
        nounBtn.Bind(wx.EVT_BUTTON, self.addNoun)
        verbBtn.Bind(wx.EVT_BUTTON, self.addVerb)
        adjBtn.Bind(wx.EVT_BUTTON, self.addAdj)
        adverbBtn.Bind(wx.EVT_BUTTON, self.addAdverbs)

        #Hide/Show buttons
        #data = loadPickle("words.txt")
        #languages = list(data[list(data)[0]])
        #for count, lang in enumerate(languages):
            #showHideBtn = wx.Button(self.langPanel, label="Hide En", size=wx.Size(50,50), pos=wx.Point(25,200))
            #showHideBtn = ShowButton(self.langPanel, lbl=f"Hide {lang}", sz=wx.Size(75, 50), ps=wx.Point(25 + count*90 ,200))
            #showHideBtn.Bind(wx.EVT_BUTTON, self.showHide)

        delBtn = wx.Button(self.langPanel,label="Delete Selected Section",size=wx.Size(150,50),pos=wx.Point(250,425))
        delBtn.Bind(wx.EVT_BUTTON,self.deleteSection)
         
        self.addLangBox = wx.TextCtrl(self.langPanel,-1,"",wx.Point(175,150))
        self.addLangBox.SetInsertionPoint(0)
        addLangBtn = wx.Button(self.langPanel,label="Add Language: ", size=wx.Size(135,23),pos=wx.Point(25,150))
        addLangBtn.Bind(wx.EVT_BUTTON, self.addLang)
        self.removeLangBox = wx.TextCtrl(self.langPanel,-1,"",wx.Point(475,150))
        self.removeLangBox.SetInsertionPoint(0)
        remLangBtn = wx.Button(self.langPanel,label="Remove Language: ", size=wx.Size(135,23),pos=wx.Point(325,150))
        remLangBtn.Bind(wx.EVT_BUTTON, self.removeOnClick)

    #Add a language to the grid
    def addLang(self,e):
        lang = self.addLangBox.GetLineText(0)
        numLangs = loadPickle("numLangs.txt")
        try:
            addLanguage(lang)
            numLangs = numLangs + 1
            dumpPickle("numLangs.txt",numLangs)
        except:
            print("Didnt' succesfully add language")

        self.grid.ClearGrid()
        newWords = loadPickle(f"{self.currentGrid}.txt")
        displayWords(self.grid, newWords)
        

    #Remove a language from the grid  
    def removeOnClick(self,e):
        language = self.removeLangBox.GetLineText(0)
        #language = language.lower()
        words = loadPickle("words.txt")
        
        if (language not in words[list(words.keys())[0]]):
            box2 = wx.MessageDialog(None,f"THat language is not in the data, Please enter language exactly as seen on the table","Remove Language",wx.OK)
            box2.Destroy()
        else:
            NO = 5104
            YES = 5103
            box = wx.MessageDialog(None,f"Are you sure you want to permanently remove {language}?",f"Remove {language}",wx.YES_NO)
            response = box.ShowModal()
            box.Destroy()
            if (response == YES):
                self.removeLang(language)
            else:
                return

    
    def removeLang(self, lang):
        numLangs = loadPickle("numLangs.txt")
        try:
            delLanguage(lang)
            numLangs = numLangs - 1
            dumpPickle("numLangs.txt", numLangs)
        except:
            print("Something went wrong, remove language didn't work")
        
        self.grid.ClearGrid()
        data = loadPickle(f"{self.currentGrid}.txt")
        for i in range(numLangs):
            if self.grid.GetColLabelValue(i) == lang:
                self.grid.HideCol(i) 
        displayWords(self.grid, data)
        return   



    #Action handler to update the grid
    def OnChangeCell(self, e):
        #Change it so it only opens one fd and then dumps to the fd at the bottom
        if (self.currentGrid == "Vocab"):
            dic = loadPickle("words.txt")
        elif (self.currentGrid == "Adverbs"):
            dic = loadPickle("Adverbs.txt")
        elif (self.currentGrid == "Verbs"):
            dic = loadPickle("Verbs.txt")
        elif (self.currentGrid == "Adjectives"):
            dic = loadPickle("Adjectives.txt")
        elif (self.currentGrid == "Prepositions"):
            dic = loadPickle("Prepositions.txt")
        elif (self.currentGrid == "Other"):
            dic = loadPickle("Other.txt")
        elif (self.currentGrid in self.sections):
            dic = loadPickle(f"{self.sections[self.currentGrid]}")
        elif (self.currentGrid in self.nounList):
            dic = loadPickle(f"{self.nounList[self.currentGrid]}")
        elif (self.currentGrid in self.adjectiveList):
            dic = loadPickle(f"{self.adjectiveList[self.currentGrid]}")
        elif (self.currentGrid in self.adverbList):
            dic = loadPickle(f"{self.adverbList[self.currentGrid]}")
        elif (self.currentGrid in self.verbList):
            dic = loadPickle(f"{self.verbList[self.currentGrid]}")
        else:
            dic = loadPickle(f"{self.otherList[self.currentGrid]}")
            
        col = e.GetCol()
        row = e.GetRow()
        lang = self.grid.GetColLabelValue(col)
        oldWord = e.GetString()
        newWord = self.grid.GetCellValue(row , col)
        #global numLangs
        numberOfLangs = len(dic[list(dic)[0]])
        translator = gt.Translator()
        if (lang == 'English'):
            if (newWord == ""):
                dic.pop(oldWord)
            else:
                dic[newWord] = {}   
                for i in range(1,numberOfLangs+1):
                    fCol = self.grid.GetColLabelValue(i)
                    foreignWord = self.grid.GetCellValue(row, i)
                    if foreignWord == "":
                        dic[newWord][fCol] = translator.translate(newWord, dest=fCol).text
                    else:
                        dic[newWord][fCol] = foreignWord
        else:
            engWord = self.grid.GetCellValue(row, 0)
            if (engWord !=  ""):
                dic[engWord][lang] = newWord

        if (self.currentGrid == "Vocab"):
            dumpPickle("words.txt",dic)
        elif (self.currentGrid == "Adverbs"):
            dumpPickle("Adverbs.txt",dic)
        elif (self.currentGrid == "Adjectives"):
            dumpPickle("Adjectives.txt",dic)
        elif (self.currentGrid == "Verbs"):
            dumpPickle("Verbs.txt",dic)
        elif (self.currentGrid == "Prepositions"):
            dumpPickle("Prepositions.txt",dic)
        elif (self.currentGrid == "Other"):
            dumpPickle("Other.txt",dic)
        elif (self.currentGrid in self.nounList):
            dumpPickle(f"{self.nounList[self.currentGrid]}",dic)
        elif (self.currentGrid in self.adjectiveList):
            dumpPickle(f"{self.adjectiveList[self.currentGrid]}",dic)
        elif (self.currentGrid in self.adverbList):
            dumpPickle(f"{self.adverbList[self.currentGrid]}",dic)
        elif (self.currentGrid in self.verbList):
            dumpPickle(f"{self.verbList[self.currentGrid]}",dic)
        elif (self.currentGrid in self.otherList):
            dumpPickle(f"{self.otherList[self.currentGrid]}",dic)
            new = loadPickle(f"{self.otherList[self.currentGrid]}")            ###########DO THIS FOR EVERYTHING IN THIS LOOP
            displayWords(self.grid, new)
        else:
            dumpPickle(f"{self.sections[self.currentGrid]}",dic)
            
    #Adds newly created section file to appropriate tree section
    def addFile(self,label,section):
        dic = {}
        if (section == "Nouns"):
            self.nounList[f"{label}"] = f"{label}.txt" #Pickle this and dump to a list txt file
            dumpPickle("nounSections.txt",self.nounList)   #Add section to list
            dumpPickle(f"{label}.txt",dic)                 #Add new data file for section
        elif (section == "Adjectives"):
            self.adjectiveList[f"{label}"] = f"{label}.txt" 
            dumpPickle("adjSections.txt",self.adjectiveList)
            dumpPickle(f"{label}.txt",dic)
        elif (section == "Verbs"):
            self.verbList[f"{label}"] = f"{label}.txt" 
            dumpPickle("verbSections.txt",self.verbList)
            dumpPickle(f"{label}.txt",dic)
        elif (section == "Adverbs"):
            self.adverbList[f"{label}"] = f"{label}.txt" 
            dumpPickle("adverbSections.txt",self.adverbList)
            dumpPickle(f"{label}.txt",dic)
        else:
            self.otherList[f"{label}"] = f"{label}.txt" 
            dumpPickle("otherSections.txt",self.otherList)
            dumpPickle(f"{label}.txt",dic)
            
    def addNoun(self,e):
        newSection = self.enterNoun.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.nouns,recursively=False)
        self.newLabel = self.tree.InsertItem(self.nouns, idx, newSection)
        self.addFile(newSection,"Nouns")
    def addVerb(self,e):
        newSection = self.enterVerb.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.verbs,recursively=False)
        self.newLabel = self.tree.InsertItem(self.verbs, idx, newSection)
        self.addFile(newSection,"Verbs")
    def addAdj(self,e):
        newSection = self.enterAdj.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.adjectives,recursively=False)
        self.newLabel = self.tree.InsertItem(self.adjectives, idx, newSection)
        self.addFile(newSection,"Adjectives")
    def addAdverbs(self,e):
        newSection = self.enterAdverb.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.adverbs,recursively=False)
        self.newLabel = self.tree.InsertItem(self.adverbs, idx, newSection)
        self.addFile(newSection,"Adverbs")
    def addOther(self,e):
        newSection = self.enterOther.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.other,recursively=False)
        self.newLabel = self.tree.InsertItem(self.other, idx, newSection)
        self.addFile(newSection,"Other")
        
    
    def showHide(self, e):
        obj = e.GetEventObject()
        label = obj.GetLabel()
        action = label[0:4]
        
        if action == "Hide":
            self.grid.HideCol(0)
            obj.SetLabel("Show" + label[4:])
        elif action == "Show":
            self.grid.ShowCol(0)
            obj.SetLabel("Hide" + label[4:])
        
    def ChangeContent(self,e):
        #Add conditional to check which was selected
        item = self.tree.GetItemText(e.GetItem()) 
        if (item != self.currentGrid):
            self.grid.ClearGrid()
            self.currentGrid = item
            if (item=="words"):
                dic = loadPickle("words.txt")
                self.grid.ClearGrid()
                displayWords(self.grid, dic)
            else:
                dic = loadPickle(f"{item}.txt")  
                if (len(dic) > 0):
                    displayWords(self.grid, dic)
                    
    def deleteSection(self,e):
        #Check parent -> THen remove from that sectionList and pickle -> remove node with function
        NO = 5104
        YES = 5103
        box = wx.MessageDialog(None,"Are you sure you want to delete the selected section?","Delete Section",wx.YES_NO)
        response = box.ShowModal()
        box.Destroy()
        if (response == YES):
            treeItem = self.tree.GetFocusedItem()  #wx TreeItem
            title = self.tree.GetItemText(treeItem)
            deletedParent = self.tree.GetItemParent(treeItem)  #wx TreeItem of parent
            self.tree.Delete(treeItem)
            
            if (self.tree.GetItemText(deletedParent) == "Nouns"):
                with open("nounSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("nounSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Adjectives"):
                with open("adjSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("adjSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Adverbs"):
                with open("adverbSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("adverbSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Prepositions"):
                with open("prepSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("prepSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Verbs"):
                with open("verbSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("verbSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Other"):
                with open("otherSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("otherSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            
            if (os.path.exists(f"{title}.txt")):
                os.remove(f"{title}.txt")
        elif (response == NO):
            print("goodbye govna.")
        else:
            pass

        self.grid.ClearGrid()
          
app = wx.App()
frame = TestFrame()
frame.Show()
app.MainLoop()
