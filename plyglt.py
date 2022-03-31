from ast import dump
from wx.core import DF_BITMAP, GREEN, YES_NO
import wx
import wx.grid
import os
import pickle
import googletrans as gt
#from utils import loadPickle, dumpPickle, displayWords, numLangs, getLanguageAbbrev, getLanguageName
from utils import *

class ShowButton(wx.Button):
    def __init__(self, parent, lbl, sz, ps):
        wx.Button.__init__(self,parent,id=wx.ID_ANY, label=lbl, size=sz, pos=ps)
        btn = wx.Button(parent, label=lbl, size=sz, pos=ps)
        btn.Bind(wx.EVT_BUTTON, TestFrame.showHide)


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="PolyGlot",
                          size=(640,480)) 
        
        #Global Variables for Entire Frame
        self.autoFillOn = True
        self.numLangs = loadPickle("./Sections/numLangs.txt")
        self.rootIdx = 2
        self.vocabIdx = 2
        self.currentGrid = "words"
        self.nounList = loadPickle("./Sections/nounSections.txt")
        self.adjectiveList = loadPickle("./Sections/adjSections.txt")
        self.adverbList = loadPickle("./Sections/adverbSections.txt")
        self.verbList = loadPickle("./Sections/verbSections.txt")
        self.otherList = loadPickle("./Sections/otherSections.txt") 
        self.sections = loadPickle("./Sections/sections.txt")

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
        self.gridPanel = wx.Panel(self, size=wx.Size(1025,1000), pos=wx.Point(150,0))
        self.grid = wx.grid.Grid(self.gridPanel,size=wx.Size(1025,1000))
        self.grid.CreateGrid(1000 ,self.numLangs + 3)
        self.grid.SetDefaultCellBackgroundColour(wx.Colour(255,255,255))
        self.grid.SetDefaultCellOverflow(False)
        self.grid.SetDefaultCellFont(wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_MEDIUM))
        self.grid.EnableGridLines(True)
        dic = loadPickle("./Sections/words.txt")
        #sortedDic = sortDic(dic)
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
        self.nounBtn = wx.Button(self.langPanel, label="Add Noun Category: ", size=wx.Size(135,23), pos=wx.Point(25,15))
        self.verbBtn = wx.Button(self.langPanel, label="Add Verb Category: ", size=wx.Size(135,23), pos=wx.Point(25,40))
        self.adjBtn = wx.Button(self.langPanel, label="Add Adjective Category: ", size=wx.Size(135,23), pos=wx.Point(25,65))
        self.adverbBtn = wx.Button(self.langPanel, label="Add Adverb Category: ", size=wx.Size(135,23), pos=wx.Point(25,90))
        self.otherBtn = wx.Button(self.langPanel, label="Add Other Category: ", size=wx.Size(135,23), pos=wx.Point(25,115))
        self.otherBtn.Bind(wx.EVT_BUTTON, self.addOther)
        self.nounBtn.Bind(wx.EVT_BUTTON, self.addNoun)
        self.verbBtn.Bind(wx.EVT_BUTTON, self.addVerb)
        self.adjBtn.Bind(wx.EVT_BUTTON, self.addAdj)
        self.adverbBtn.Bind(wx.EVT_BUTTON, self.addAdverbs)

        #Hide/Show buttons
        showHideEng = ShowButton(self.langPanel, lbl=f"Hide English", sz=wx.Size(75, 50), ps=wx.Point(25 ,200))
        showHideEng.Bind(wx.EVT_BUTTON, self.showHide)
        data = loadPickle("./Sections/words.txt")
        languages = list(data[list(data)[0]])
        for count, lang in enumerate(languages):
            
            showHideBtn = ShowButton(self.langPanel, lbl=f"Hide {lang}", sz=wx.Size(75, 50), ps=wx.Point(25 + (count % 6 + 1) * 90 , (200 if count < 6 else 270)))
            showHideBtn.Bind(wx.EVT_BUTTON, self.showHide)

        shuffleBtn = wx.Button(self.langPanel, label="Shuffle\nWords", size=wx.Size(120,60),pos=wx.Point(400,40))
        shuffleBtn.Bind(wx.EVT_BUTTON, self.shuffleWords)
        sortBtn = wx.Button(self.langPanel, label="Sort\nWords", size=wx.Size(120,60),pos=wx.Point(600,40))
        sortBtn.Bind(wx.EVT_BUTTON, self.sortWords)


        fillBtn = wx.Button(self.langPanel, label="Auto-Fill Empty Words", size=wx.Size(150,60), pos=wx.Point(450,425))
        fillBtn.Bind(wx.EVT_BUTTON, self.autoFill)

        autoToggleBtn = wx.Button(self.langPanel, label="Turn Auto Fill Off", size=wx.Size(150,60), pos=wx.Point(300,325))
        autoToggleBtn.Bind(wx.EVT_BUTTON, self.toggleAuto)

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


    def toggleAuto(self,e):
        obj = e.GetEventObject()
        option = obj.GetLabel()
        option = option[-3:]
        print(option)
        if option == "Off":
            self.autoFillOn = False
            obj.SetLabel("Turn Auto Fill On")
        elif option == " On":
            self.autoFillOn = True
            obj.SetLabel("Turn Auto Fill Off")
        
        


    def autoFill(self, e):
        dlg = wx.TextEntryDialog(frame, 'Enter the language as shown in the column header','Auto Fill Words')
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            language = dlg.GetValue().lower()
        dlg.Destroy()
        language = language[0].upper() + language[1:]
        print(language)
        data = loadPickle(f"./Sections/{self.currentGrid}.txt")
        if language.lower() == "mandarin":
            try:
                for k in data:
                    if data[k][language] == "":
                        data[k][language] = gt.Translator().translate(k, dest="zh-CN").text 
                    else:
                        continue
            except:
                print("Sorry bud, didn't work for some reason. Don't kill yourself.")

        try:
            for k in data:
                if data[k][language] == "":
                
                    data[k][language] = gt.Translator().translate(k, dest=language).text 
                else:
                    continue
        except:
            print("Can't find that language with Googie Trans\n Sorry \n Don't give up!!!")
        displayWords(self.grid, data)
        dumpPickle(f"./Sections/{self.currentGrid}.txt" , data)
        


    def showHide(self, e):
        obj = e.GetEventObject()
        label = obj.GetLabel()
        action = label[0:4]
        languageToHide = label[5:]
        languages = loadPickle("./Sections/words.txt")
        languages = list(languages[list(languages.keys())[0]])
        
        if languageToHide == "English" and action == "Hide":
            self.grid.HideCol(0)
            obj.SetLabel("Show English")
        elif action == "Show" and languageToHide == "English":
            self.grid.ShowCol(0)
            obj.SetLabel("Hide English")
        elif action == "Hide":
            for idx in range(len(languages)):
                if languages[idx] == languageToHide:
                    self.grid.HideCol(idx+1)
            obj.SetLabel("Show" + label[4:])
        elif action == "Show":
            for idx in range(len(languages)):
                if languages[idx] == languageToHide:
                    self.grid.ShowCol(idx+1)
            obj.SetLabel("Hide" + label[4:])

    
    def shuffleWords(self,e):
        dic = loadPickle(f"./Sections/{self.currentGrid}.txt")
        
        shuffled = shuffleDic(dic)
        displayWords(self.grid, shuffled)
       
        
    def sortWords(self,e):
        dic = loadPickle(f"./Sections/{self.currentGrid}.txt")
        alpha = sortDic(dic)
        displayWords(self.grid, alpha)    


    #Add a language to the grid
    def addLang(self,e):
        lang = self.addLangBox.GetLineText(0)
        self.addLangBox.SetLabelText("")
        numLangs = loadPickle("./Sections/numLangs.txt")
        try:
            addLanguage(lang)
            numLangs = numLangs + 1
            dumpPickle("./Sections/numLangs.txt",numLangs)
        except:
            print("Didnt' succesfully add language")

        self.grid.ClearGrid()
        newWords = loadPickle(f"./Sections/{self.currentGrid}.txt")
        displayWords(self.grid, newWords)
        

    #Remove a language from the grid  
    def removeOnClick(self,e):
        language = self.removeLangBox.GetLineText(0)
        self.removeLangBox.SetLabelText("")
        #language = language.lower()
        words = loadPickle("./Sections/words.txt")
        
        if (language not in words[list(words.keys())[0]] and language != 'English'):
            box2 = wx.MessageDialog(None,f"THat language is not in the data, Please enter language exactly as seen on the table","Remove Language",wx.OK)
            box2.Destroy()
        elif (language == 'English'):
            box2 = wx.MessageDialog(None,f"English cannot be removed, the words for all languages are stored with relation to their English counterpart","Remove Language",wx.OK)
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

    #DOn't allow english to be removed
    def removeLang(self, lang):
        numLangs = loadPickle("./Sections/numLangs.txt")
        try:
            delLanguage(lang)
            numLangs = numLangs - 1
            dumpPickle("./Sections/numLangs.txt", numLangs)
        except:
            print("Something went wrong, remove language didn't work")
        
        self.grid.ClearGrid()
        data = loadPickle(f"./Sections/{self.currentGrid}.txt")
        for i in range(numLangs):
            if self.grid.GetColLabelValue(i) == lang:
                self.grid.DeleteCols(i) 
        displayWords(self.grid, data)
        return   



    #Action handler to update the grid
    def OnChangeCell(self, e):
        
        isAutoFill = self.autoFillOn

        #Change it so it only opens one fd and then dumps to the fd at the bottom
        if (self.currentGrid == "words"):
            dic = loadPickle("./Sections/words.txt")
        elif (self.currentGrid == "Adverbs"):
            dic = loadPickle("./Sections/Adverbs.txt")
        elif (self.currentGrid == "Verbs"):
            dic = loadPickle("./Sections/Verbs.txt")
        elif (self.currentGrid == "Adjectives"):
            dic = loadPickle("./Sections/Adjectives.txt")
        elif (self.currentGrid == "Prepositions"):
            dic = loadPickle("./Sections/Prepositions.txt")
        elif (self.currentGrid == "Other"):
            dic = loadPickle("./Sections/Other.txt")
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
        numberOfLangs = len(dic[list(dic)[0]])
        translator = gt.Translator()
        if (lang == 'English'):    #If english was changed -> THen....
            if (newWord == ""):
                dic.pop(oldWord)
            else:
                if newWord not in dic:
                    dic[newWord] = {}   
                    for i in range(1,numberOfLangs+1):
                        fCol = self.grid.GetColLabelValue(i)
                        foreignWord = self.grid.GetCellValue(row, i)
                        if foreignWord == "" and self.autoFillOn:
                            try:
                                dic[newWord][fCol] = translator.translate(newWord, dest=fCol).text
                            except:
                                print("Language not recognized by Google translate")
                        else:
                            dic[newWord][fCol] = foreignWord
        else: #Some other language was changed
            
            engWord = self.grid.GetCellValue(row, 0)
            if (engWord !=  ""):
                dic[engWord][lang] = newWord
            
                for i in range(1,numberOfLangs+1):
                    fWord = self.grid.GetCellValue(row, i)
                    flang = self.grid.GetColLabelValue(i)
                    if fWord == "" and flang != lang and self.autoFillOn:  #Only if there is not foreign word currently
                        dic[engWord][flang] = translator.translate(engWord, dest=flang).text
                    else:
                        continue
            
            else:  #English word is emtpy and foreign lanugae cell has been changed
                english = translator.translate(newWord, dest="en").text
                dic[english] = {}
                
                for i in range(1,numberOfLangs+1):
                    flang = self.grid.GetColLabelValue(i)
                    dic[english][flang] = translator.translate(english, dest=flang).text
            

        if (self.currentGrid == "words"):
            dumpPickle("./Sections/words.txt",dic)
            new = loadPickle("./Sections/words.txt")           
            displayWords(self.grid, new)
        elif (self.currentGrid == "Adverbs"):
            dumpPickle("./Sections/Adverbs.txt",dic)
            new = loadPickle("./Sections/Adverbs.txt")           
            displayWords(self.grid, new)
        elif (self.currentGrid == "Adjectives"):
            dumpPickle("./Sections/Adjectives.txt",dic)
            new = loadPickle(f"./Sections/Adjectives.txt")     
            displayWords(self.grid, new)
        elif (self.currentGrid == "Verbs"):
            dumpPickle("./Sections/Verbs.txt",dic)
            new = loadPickle("./Sections/Verbs.txt")           
            displayWords(self.grid, new)
        elif (self.currentGrid == "Prepositions"):
            dumpPickle("./Sections/Prepositions.txt",dic)
            new = loadPickle("./Sections/Prepositions.txt")           
            displayWords(self.grid, new)
        elif (self.currentGrid == "Other"):
            dumpPickle("./Sections/Other.txt",dic)
            new = loadPickle("./Sections/Other.txt")           
            displayWords(self.grid, new)
        elif (self.currentGrid in self.nounList):
            dumpPickle(f"{self.nounList[self.currentGrid]}",dic)
            new = loadPickle(f"{self.nounList[self.currentGrid]}")           
            displayWords(self.grid, new)
        elif (self.currentGrid in self.adjectiveList):
            dumpPickle(f"{self.adjectiveList[self.currentGrid]}",dic)
            new = loadPickle(f"{self.adjectiveList[self.currentGrid]}")            
            displayWords(self.grid, new)
        elif (self.currentGrid in self.adverbList):
            dumpPickle(f"{self.adverbList[self.currentGrid]}",dic)
            new = loadPickle(f"{self.adverbList[self.currentGrid]}")            
            displayWords(self.grid, new)
        elif (self.currentGrid in self.verbList):
            dumpPickle(f"{self.verbList[self.currentGrid]}",dic)
            new = loadPickle(f"{self.verbList[self.currentGrid]}")            
            displayWords(self.grid, new)
        elif (self.currentGrid in self.otherList):
            dumpPickle(f"{self.otherList[self.currentGrid]}",dic)
            new = loadPickle(f"{self.otherList[self.currentGrid]}")            
            displayWords(self.grid, new)
        else:
            dumpPickle(f"{self.sections[self.currentGrid]}",dic)
            new = loadPickle(f"{self.sections[self.currentGrid]}")            
            displayWords(self.grid, new)
            
    #Adds newly created section file to appropriate tree section
    def addFile(self,label,section):
        #Load data -> Grab current languages -> Initalize them in the dic variable
        d = loadPickle("./Sections/words.txt")
        langs = list(d[list(d)[0]])
        dic = {"Enter here": {}}
        for l in langs:
            dic["Enter here"][l] = ""


        if (section == "Nouns"):
            self.nounList[f"{label}"] = f"./Sections/{label}.txt" #Pickle this and dump to a list txt file
            dumpPickle("./Sections/nounSections.txt",self.nounList)   #Add section to list
            dumpPickle(f"./Sections/{label}.txt",dic)                 #Add new data file for section
        elif (section == "Adjectives"):
            self.adjectiveList[f"{label}"] = f"./Sections/{label}.txt" 
            dumpPickle("./Sections/adjSections.txt",self.adjectiveList)
            dumpPickle(f"./Sections/{label}.txt",dic)
        elif (section == "Verbs"):
            self.verbList[f"{label}"] = f"./Sections/{label}.txt" 
            dumpPickle("./Sections/verbSections.txt",self.verbList)
            dumpPickle(f"./Sections/{label}.txt",dic)
        elif (section == "Adverbs"):
            self.adverbList[f"{label}"] = f"./Sections/{label}.txt" 
            dumpPickle("./Sections/adverbSections.txt",self.adverbList)
            dumpPickle(f"./Sections/{label}.txt",dic)
        else:
            self.otherList[f"{label}"] = f"./Sections/{label}.txt" 
            dumpPickle("./Sections/otherSections.txt",self.otherList)
            dumpPickle(f"./Sections/{label}.txt",dic)
            
    def addNoun(self,e):
        newSection = self.enterNoun.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.nouns,recursively=False)
        self.newLabel = self.tree.InsertItem(self.nouns, idx, newSection)
        self.addFile(newSection,"Nouns")
        self.enterNoun.SetLabelText("")
    def addVerb(self,e):
        newSection = self.enterVerb.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.verbs,recursively=False)
        self.newLabel = self.tree.InsertItem(self.verbs, idx, newSection)
        self.addFile(newSection,"Verbs")
        self.enterVerb.SetLabelText("")
    def addAdj(self,e):
        newSection = self.enterAdj.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.adjectives,recursively=False)
        self.newLabel = self.tree.InsertItem(self.adjectives, idx, newSection)
        self.addFile(newSection,"Adjectives")
        self.enterAdj.SetLabelText("")
    def addAdverbs(self,e):
        newSection = self.enterAdverb.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.adverbs,recursively=False)
        self.newLabel = self.tree.InsertItem(self.adverbs, idx, newSection)
        self.addFile(newSection,"Adverbs")
        self.enterAdverb.SetLabelText("")
    def addOther(self,e):
        newSection = self.enterOther.GetLineText(0)
        idx = self.tree.GetChildrenCount(self.other,recursively=False)
        self.newLabel = self.tree.InsertItem(self.other, idx, newSection)
        self.addFile(newSection,"Other")
        self.enterOther.SetLabelText("")
    
        
    def ChangeContent(self,e):
        #Add conditional to check which was selected
        item = self.tree.GetItemText(e.GetItem()) 
        if (item != self.currentGrid):
            self.grid.ClearGrid()
            self.currentGrid = item
            if (item=="words"):
                dic = loadPickle("./Sections/words.txt")
                self.grid.ClearGrid()
                sorted = sortDic(dic)
                displayWords(self.grid, sorted)
            else:
                dic = loadPickle(f"./Sections/{item}.txt")  
                sorted = sortDic(dic)
                if (len(dic) > 0):
                    displayWords(self.grid, sorted)
                    
    def deleteSection(self,e):
        #Check parent -> THen remove from that sectionList and pickle -> remove node with function
        NO = 5104
        YES = 5103
        treeItem = self.tree.GetFocusedItem()  #wx TreeItem
        title = self.tree.GetItemText(treeItem)
        box = wx.MessageDialog(None,f"Are you sure you want to delete the {title} section?","Delete Section",wx.YES_NO)
        response = box.ShowModal()
        box.Destroy()
        if (response == YES):
              
            deletedParent = self.tree.GetItemParent(treeItem)  #wx TreeItem of parent
            self.tree.Delete(treeItem)
            
            if (self.tree.GetItemText(deletedParent) == "Nouns"):
                with open("./Sections/nounSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("./Sections/nounSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Adjectives"):
                with open("./Sections/adjSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("./Sections/adjSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Adverbs"):
                with open("./Sections/adverbSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("./Sections/adverbSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Prepositions"):
                with open("./Sections/prepSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("./Sections/prepSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Verbs"):
                with open("./Sections/verbSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("./Sections/verbSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            elif (self.tree.GetItemText(deletedParent) == "Other"):
                with open("./Sections/otherSections.txt","rb") as fd:
                    dic = pickle.load(fd)
                    if (dic[title]):
                        dic.pop(title)
                with open("./Sections/otherSections.txt","wb") as fd:
                    pickle.dump(dic,fd)
            
            if (os.path.exists(f"./Sections/{title}.txt")):
                os.remove(f"./Sections/{title}.txt")
        elif (response == NO):
            print("goodbye govna.")
        else:
            pass

        self.grid.ClearGrid()
          
app = wx.App()
frame = TestFrame()
frame.Show()
app.MainLoop()
