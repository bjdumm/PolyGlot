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
        self.currentGrid = "Vocab"
        self.sections = {}
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
        self.vocab = self.tree.InsertItem(root,0,"Vocab")   #Vocab section
        self.adjectives = self.tree.InsertItem(self.vocab,0,"Adjectives")
        self.Nouns = self.tree.InsertItem(self.vocab,1,"Nouns")
        self.verbs = self.tree.InsertItem(root,1,"Verbs")  #Verbs Section
        self.tree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.ChangeContent)

        #Center Grid
        self.gridPanel = wx.Panel(self, size=wx.Size(1000,1000), pos=wx.Point(150,0))
        self.grid = wx.grid.Grid(self.gridPanel,size=wx.Size(1000,1000))
        self.grid.CreateGrid(500 ,self.numLangs + 3)
        self.grid.SetDefaultCellBackgroundColour(wx.Colour(150,150,150))
        self.grid.SetDefaultCellOverflow(False)
        self.grid.SetDefaultCellFont(wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_MEDIUM))
        #self.EnableGridLines(False)
        displayWords(self.grid, words.vocab)
        self.grid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.OnChange)

        #Language Panel RHS
        self.langPanel = wx.Panel(self,pos=wx.Point(1200,0),size=wx.Size(750,500))
        enterLang = wx.TextCtrl(self.langPanel, -1, "Enter language", wx.Point(175,15))
        enterLang.SetInsertionPoint(0)
        btn = wx.Button(self.langPanel, label="Add New Language: ", size=wx.Size(125,50), pos=wx.Point(25,0))
        btn.Bind(wx.EVT_BUTTON, self.OnClick)
        #Add buttons to Hide/Show each language (use parity flags to render new grid) 
        #Create render funciton that takes number of columsn as arg, pass it current - 1 args when language is hidden

    
    ####Handler functions####
    #Action handler to update the grid
    def OnChange(self, e):
        if (self.currentGrid == "Vocab"):
            dic = words.vocab
        elif (self.currentGrid == "Verbs"):
            dic = words.verbs
        elif(self.currentGrid == "Adjectives"):
            dic = words.adjectives
        elif(self.currentGrid == "Nouns"):
            dic = words.nouns
        
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
        elif (self.currentGrid == "Verbs"):
            with open(f'{self.currentGrid}.txt','wb') as fh:
                pickle.dump(dic, fh)
        elif (self.currentGrid == "Nouns"):
            with open(f'{self.currentGrid}.txt','wb') as fh:
                pickle.dump(dic, fh)
        elif (self.currentGrid == "Adjectives"):
            with open(f'{self.currentGrid}.txt' , 'wb') as fh:
                pickle.dump(dic,fh)
        
    
    
    def OnClick(self,e):
        self.tree.SetBackgroundColour(wx.Colour(255,0,0))
        
    def ChangeContent(self,e):
        #Add conditional to check which was selected
        item = self.tree.GetItemText(e.GetItem())
        if (item == "Nouns"):
            self.grid.ClearGrid()
            displayWords(self.grid, words.nouns)
        elif(item == "Adjectives"):
            self.grid.ClearGrid()
            displayWords(self.grid, words.adjectives)
        elif(item == "Vocab"):
            self.grid.ClearGrid()
            displayWords(self.grid, words.vocab)
        elif(item == "Verbs"):
            self.grid.ClearGrid()
            displayWords(self.grid, words.verbs)

    


app = wx.App()
frame = TestFrame()
frame.Show()
app.MainLoop()