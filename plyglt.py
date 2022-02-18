from wx.core import DF_BITMAP, GREEN, YES_NO
import wx
import wx.grid
import os
import pickle
import words

#numLangs = 4
with open("numLangs.txt","rb") as fd:
    numLangs = pickle.load(fd)
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



class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="PolyGlot",
                          size=(640,480)) 
        
        #Global Variables for Entire Frame
        self.numLangs = 4
        self.rootIdx = 2
        self.vocabIdx = 2
        self.currentGrid = "Vocab"
        self.nounList = {}
        if os.path.exists("nounSections.txt"):
            with open("nounSections.txt","rb") as fd:
                self.nounList = pickle.load(fd)
         
        self.adjectiveList = {}
        if os.path.exists("adjSections.txt"):
            with open("adjSections.txt","rb") as fd:
                self.adjectiveList = pickle.load(fd)
        self.adverbList = {}
        if os.path.exists("adverbSections.txt"):
            with open("adverbSections.txt","rb") as fd:
                self.adverbList = pickle.load(fd)
        self.verbList = {}
        if os.path.exists("verbSections.txt"):
            with open("verbSections.txt","rb") as fd:
                self.verbList = pickle.load(fd)
        self.prepList = {}
        if os.path.exists("prepSections.txt"):
            with open("prepSections.txt","rb") as fd:
                self.prepList = pickle.load(fd)

        self.otherList = {}
        if os.path.exists("otherSections.txt"):
            with open("otherSections.txt","rb") as fd:
                self.otherList = pickle.load(fd)
        with open("sections.txt","rb") as fd:
            self.sections = pickle.load(fd)
            
        #How about a list of nodes for noun, a lsit for verbs, etc. append to it, easy to loop and place one by one in parent. The problem
        #is newly created root level categories(Maybe just don't allow that. Add preps, adverbs etc. then just have options to add new cateogry to each of those?)
        #So create wxTreeNode based on entered label, then just append that to the appropriate list
        
        #Menu Bar
        self.menuBar = wx.MenuBar()
        self.fileBtn = wx.Menu()
        self.exitItem = self.fileBtn.Append(wx.ID_FILE1, 'Select File')
        self.menuBar.Append(self.fileBtn,"File")
        self.SetMenuBar(self.menuBar)

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
        
        self.vocab = self.tree.InsertItem(root,3,"Vocab")
        
        self.adverbs = self.tree.InsertItem(root,4,"Adverbs")
        for idx, k in enumerate(self.adverbList):
            self.tree.InsertItem(self.adverbs,idx,k)

        self.preps = self.tree.InsertItem(root,5,"Prepositions")
        for idx, k in enumerate(self.prepList):
            self.tree.InsertItem(self.preps,idx,k)

        self.other = self.tree.InsertItem(root,6,"Other")
        for idx, k in enumerate(self.otherList):
            self.tree.InsertItem(self.other,idx,k)

        self.tree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.ChangeContent)
        

        #Center Grid
        self.gridPanel = wx.Panel(self, size=wx.Size(1000,1000), pos=wx.Point(150,0))
        self.grid = wx.grid.Grid(self.gridPanel,size=wx.Size(1000,1000))
        self.grid.CreateGrid(500 ,self.numLangs + 3)
        self.grid.SetDefaultCellBackgroundColour(wx.Colour(255,255,255))
        self.grid.SetDefaultCellOverflow(False)
        self.grid.SetDefaultCellFont(wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_MEDIUM))
        #self.EnableGridLines(False)
        with open("words.txt","rb") as fd:
            dic = pickle.load(fd)
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
        nounBtn = wx.Button(self.langPanel, label="Add Noun Category: ", size=wx.Size(135,23), pos=wx.Point(25,15))
        verbBtn = wx.Button(self.langPanel, label="Add Verb Category: ", size=wx.Size(135,23), pos=wx.Point(25,40))
        adjBtn = wx.Button(self.langPanel, label="Add Adjective Category: ", size=wx.Size(135,23), pos=wx.Point(25,65))
        adverbBtn = wx.Button(self.langPanel, label="Add Adverb Category: ", size=wx.Size(135,23), pos=wx.Point(25,90))
        nounBtn.Bind(wx.EVT_BUTTON, self.addNoun)
        verbBtn.Bind(wx.EVT_BUTTON, self.addVerb)
        adjBtn.Bind(wx.EVT_BUTTON, self.addAdj)
        adverbBtn.Bind(wx.EVT_BUTTON, self.addAdverbs)
        delBtn = wx.Button(self.langPanel,label="Delete Selected Section",size=wx.Size(150,50),pos=wx.Point(250,425))
        delBtn.Bind(wx.EVT_BUTTON,self.deleteSection)
        #Add buttons to Hide/Show each language (use parity flags to render new grid) 
        
        #Add Language Section
        self.addLangBox = wx.TextCtrl(self.langPanel,-1,"",wx.Point(175,150))
        self.addLangBox.SetInsertionPoint(0)
        addLangBtn = wx.Button(self.langPanel,label="Add Language: ", size=wx.Size(135,23),pos=wx.Point(25,150))
        addLangBtn.Bind(wx.EVT_BUTTON, self.addLang)

    def addLang(self,e):
        lang = self.addLangBox.GetLineText(0)
        with open("words.txt","rb") as fd:
            words = pickle.load(fd)
            for k in words:
                words[k][lang] = ""
        with open("words.txt","wb") as fd:
            pickle.dump(words,fd)
        global numLangs
        numLangs = numLangs + 1
        print(numLangs)
        with open("numLangs.txt","wb") as fd:
            pickle.dump(numLangs,fd)
        displayWords(self.grid, words)
        #You'll have to pickle the numLangs and load it at first

    #Action handler to update the grid
    def OnChangeCell(self, e):
        #Change it so it only opens one fd and then dumps to the fd at the bottom
        if (self.currentGrid == "Vocab"):
            with open("words.txt","rb") as fd:
                dic = pickle.load(fd)
        elif (self.currentGrid == "Adverbs"):
            with open("Adverbs.txt","rb") as fd:
                dic = pickle.load(fd)
        elif (self.currentGrid in self.sections):
            fd = open(f"{self.sections[self.currentGrid]}","rb")
            dic = pickle.load(fd)
            fd.close()
        elif (self.currentGrid in self.nounList):
            fd = open(f"{self.nounList[self.currentGrid]}","rb")
            dic = pickle.load(fd)
            fd.close()
        elif (self.currentGrid in self.adjectiveList):
            fd = open(f"{self.adjectiveList[self.currentGrid]}","rb")
            dic = pickle.load(fd)
            fd.close()
        elif (self.currentGrid in self.adverbList):
            fd = open(f"{self.adverbList[self.currentGrid]}","rb")
            dic = pickle.load(fd)
            fd.close()
        elif (self.currentGrid in self.verbList):
            fd = open(f"{self.verbList[self.currentGrid]}","rb")
            dic = pickle.load(fd)
            fd.close()
        elif (self.currentGrid in self.prepList):
            fd = open(f"{self.prepList[self.currentGrid]}","rb")
            dic = pickle.load(fd)
            fd.close()
        else:
            fd = open(f"{self.otherList[self.currentGrid]}","rb")
            dic = pickle.load(fd)
            fd.close()
        
        
        col = e.GetCol()
        row = e.GetRow()
        lang = self.grid.GetColLabelValue(col)
        oldWord = e.GetString()
        newWord = self.grid.GetCellValue(row , col)
        global numLangs
        if (lang == 'English'):
            if (newWord == ""):
                dic.pop(oldWord)
            else:
                dic[newWord] = {}  #later, check whether already in dictionary
                
                for i in range(numLangs):
                    fCol = self.grid.GetColLabelValue(i)
                    foreignWord = self.grid.GetCellValue(row, i)
                    dic[newWord][fCol] = foreignWord
        else:
            engWord = self.grid.GetCellValue(row, numLangs)
            if (engWord !=  ""):
                dic[engWord][lang] = newWord

        if (self.currentGrid == "Vocab"):
            with open('words.txt','wb') as fh:
                pickle.dump(dic, fh)
        elif (self.currentGrid == "Adverbs"):
            with open('Adverbs.txt','wb') as fh:
                pickle.dump(dic, fh)
        elif (self.currentGrid in self.nounList):
            with open(f"{self.nounList[self.currentGrid]}",'wb') as fh:
                pickle.dump(dic,fh)
        elif (self.currentGrid in self.adjectiveList):
            with open(f"{self.adjectiveList[self.currentGrid]}",'wb') as fh:
                pickle.dump(dic,fh)
        elif (self.currentGrid in self.adverbList):
            with open(f"{self.adverbList[self.currentGrid]}",'wb') as fh:
                pickle.dump(dic,fh)
        elif (self.currentGrid in self.verbList):
            with open(f"{self.verbList[self.currentGrid]}",'wb') as fh:
                pickle.dump(dic,fh)
        else:
            with open(f"{self.sections[self.currentGrid]}",'wb') as fh:
                pickle.dump(dic, fh)
        
        
    def addFile(self,label,section):
        if (section == "Nouns"):
            self.nounList[f"{label}"] = f"{label}.txt" #Pickle this and dump to a list txt file
            with open("nounSections.txt","wb") as f:
                pickle.dump(self.nounList,f)
            dic = {}
            with open(f"{label}.txt","wb") as fd:
                pickle.dump(dic, fd)
        elif (section == "Adjectives"):
            self.adjectiveList[f"{label}"] = f"{label}.txt" 
            with open("adjSections.txt","wb") as f:
                pickle.dump(self.adjectiveList,f)
            dic = {}
            with open(f"{label}.txt","wb") as fd:
                pickle.dump(dic, fd)
        elif (section == "Verbs"):
            self.verbList[f"{label}"] = f"{label}.txt" 
            with open("verbSections.txt","wb") as f:
                pickle.dump(self.verbList,f)
            dic = {}
            with open(f"{label}.txt","wb") as fd:
                pickle.dump(dic, fd)
        elif (section == "Adverbs"):
            self.adverbList[f"{label}"] = f"{label}.txt" 
            with open("adverbSections.txt","wb") as f:
                pickle.dump(self.adverbList,f)
            dic = {}
            with open(f"{label}.txt","wb") as fd:
                pickle.dump(dic, fd)
        else:
            pass
        
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
        
        
    def ChangeContent(self,e):
        #Add conditional to check which was selected
        item = self.tree.GetItemText(e.GetItem()) 
        if (item != self.currentGrid):
            self.grid.ClearGrid()
            self.currentGrid = item
            if (item=="Vocab"):
                with open("words.txt" , 'rb') as f:
                    dic = pickle.load(f)
                    self.grid.ClearGrid()
                    displayWords(self.grid, dic)
            else:
                with open(f"{item}.txt","rb") as f:
                    dic = pickle.load(f)
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



"""def addSection(self,e):
        self.tree.SetBackgroundColour(wx.Colour(255,0,0))
        newSection = self.enterNoun.GetLineText(0)
        parent = self.tree.GetFocusedItem()
        idx = self.tree.GetChildrenCount(parent,recursively=False)
        self.newLabel = self.tree.InsertItem(parent, idx, newSection)
        self.addFile(newSection)
        with open("sections.txt","rb") as fd:
            sec = pickle.load(fd)
            sec[newSection] = f"{newSection}.txt"
            with open("sections.txt","wb") as f:
                pickle.dump(sec,f)
"""