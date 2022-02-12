from wx.core import DF_BITMAP, GREEN
import wx
import wx.grid
import words
import pickle


numLangs = 4

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
        with open("sections.txt","rb") as fd:
            self.sections = pickle.load(fd)
            print(self.sections)
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
        self.Nouns = self.tree.InsertItem(root,1,"Nouns")
        self.verbs = self.tree.InsertItem(root,2,"Verbs")  #Verbs Section
        self.vocab = self.tree.InsertItem(root,3,"Vocab")
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
        self.grid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.OnChange)

        #Language Panel RHS
        self.langPanel = wx.Panel(self,pos=wx.Point(1200,0),size=wx.Size(750,500))
        self.enterNoun = wx.TextCtrl(self.langPanel, -1,"", wx.Point(175,15))
        self.enterNoun.SetInsertionPoint(0)
        self.enterVerb = wx.TextCtrl(self.langPanel, -1,"", wx.Point(175,40))
        self.enterVerb.SetInsertionPoint(0)
        self.enterAdj = wx.TextCtrl(self.langPanel, -1,"", wx.Point(175,65))
        self.enterAdj.SetInsertionPoint(0)
        nounBtn = wx.Button(self.langPanel, label="Add Noun Category: ", size=wx.Size(125,23), pos=wx.Point(25,15))
        verbBtn = wx.Button(self.langPanel, label="Add Verb Category: ", size=wx.Size(125,23), pos=wx.Point(25,40))
        adjBtn = wx.Button(self.langPanel, label="Add Adjective Category: ", size=wx.Size(135,23), pos=wx.Point(25,65))
        nounBtn.Bind(wx.EVT_BUTTON, self.OnClick)
        #Add buttons to Hide/Show each language (use parity flags to render new grid) 
        #Create render funciton that takes number of columsn as arg, pass it current - 1 args when language is hidden

    
    #Action handler to update the grid
    def OnChange(self, e):
        #Change it so it only opens one fd and then dumps to the fd at the bottom
        if (self.currentGrid == "Vocab"):
            with open("words.txt","rb") as fd:
                dic = pickle.load(fd)
        elif (self.currentGrid in self.sections):
            fd = open(f"{self.sections[self.currentGrid]}","rb")
            dic = pickle.load(fd)
            fd.close()
        
        
        col = e.GetCol()
        row = e.GetRow()
        lang = self.grid.GetColLabelValue(col)
        oldWord = e.GetString()
        newWord = self.grid.GetCellValue(row , col)
        if (lang == 'English'):
            if (newWord == ""):
                dic.pop(oldWord)
            else:
                dic[newWord] = {}  #later, check whether already in dictionary
                
                for i in range(self.numLangs):
                    fCol = self.grid.GetColLabelValue(i)
                    foreignWord = self.grid.GetCellValue(row, i)
                    dic[newWord][fCol] = foreignWord
        else:
            engWord = self.grid.GetCellValue(row, self.numLangs)
            if (engWord !=  ""):
                dic[engWord][lang] = newWord

        if (self.currentGrid == "Vocab"):
            with open('words.txt','wb') as fh:
                pickle.dump(dic, fh)
        else:
            with open(f"{self.sections[self.currentGrid]}",'wb') as fh:
                pickle.dump(dic, fh)
        
        
    def addFile(self,label):
        if (label not in self.sections):
            self.sections[label] = f"{label}.txt"
            dic = {}
            with open(f"{label}.txt","wb") as fd:
                pickle.dump(dic, fd)
        

    
    def OnClick(self,e):
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
                with open(f"{self.sections[item]}","rb") as f:
                    dic = pickle.load(f)
                    if (len(dic) > 0):
                        displayWords(self.grid, dic)
        
        #if (item == "Nouns"):
        #    self.grid.ClearGrid()
        #    self.currentGrid = "Nouns"
        #    with open("Nouns.txt", 'rb') as f:
        #        dic = pickle.load(f)
        #        displayWords(self.grid, dic)
        #elif(item == "Adjectives"):
        #    self.grid.ClearGrid()
        #    displayWords(self.grid, words.adjectives)
        #elif(item == "Vocab"):
        #    self.grid.ClearGrid()
        #    displayWords(self.grid, words.vocab)
        #elif(item == "Verbs"):
        #    self.grid.ClearGrid()
        #    displayWords(self.grid, words.verbs)

    


app = wx.App()
frame = TestFrame()
frame.Show()
app.MainLoop()