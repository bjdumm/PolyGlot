from wx.core import GREEN
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


#Main Grid with words in it
class MyGrid(wx.grid.Grid):
    def __init__(self, parent, size):
        super(MyGrid, self).__init__(parent,size=wx.Size(700,1000))
        self.CreateGrid(500 ,numLangs + 3)
        self.SetDefaultCellBackgroundColour(wx.Colour(150,150,150))
        self.SetDefaultCellOverflow(False)
        self.SetDefaultCellFont(wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_MEDIUM))
        #self.EnableGridLines(False)
        displayWords(self, words.eng)
        self.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.OnChange)
        

    #Action handler to update the grid
    def OnChange(self, e):
        dic = words.eng
        col = e.GetCol()
        row = e.GetRow()
        lang = self.GetColLabelValue(col)
        oldWord = e.GetString()
        newWord = self.GetCellValue(row , col)
        if (lang == 'English'):
            if (newWord == ""):
                dic.pop(oldWord)
            else:
                dic[newWord] = {}  #later, check whether already in dictionary
                
                for i in range(numLangs):
                    fCol = self.GetColLabelValue(i)
                    foreignWord = self.GetCellValue(row, i)
                    dic[newWord][fCol] = foreignWord
        else:
            engWord = self.GetCellValue(row, numLangs)
            if (engWord !=  ""):
                dic[engWord][lang] = newWord

        with open('words3.txt','wb') as fh:
            pickle.dump(dic, fh)


class GridPanel(wx.Panel):
    def __init__(self, parent, size, pos):
        super(GridPanel, self).__init__(parent,size=size,pos=pos)
        grid = MyGrid(self, wx.Size(400,8000))


class langPanel(wx.Panel):

    def __init__(self, parent,grid):
        super(langPanel,self).__init__(parent,pos=wx.Point(880,0), size=wx.Size(1000,500))
        self.enterLang = wx.TextCtrl(self, -1, "Enter language", wx.Point(175,15))
        self.enterLang.SetInsertionPoint(0)
        btn = wx.Button(self, label="Add New Language: ", size=wx.Size(125,50), pos=wx.Point(25,0))
        btn.Bind(wx.EVT_BUTTON, self.OnClick)
        self.lang = ""
        self.grid = grid

    def OnClick(self, e):
        self.lang = self.enterLang.GetValue()
        #Now recall MyGrid with updated dictionary after adding new key
        dic = words.eng
        for k in dic.keys():
	        dic[k][self.lang] = ""
        with open('words3.txt', 'wb') as fh:
            pickle.dump(dic, fh)
        global numLangs
        numLangs = numLangs + 1
        displayWords(self.grid,words.eng)
        

#LHS Tree for file structure
class TreePanel(wx.Panel):
    def __init__(self, parent, size, pos):
        super(TreePanel, self).__init__(parent, size=size, pos=pos)
        tree = wx.TreeCtrl(self,size=wx.Size(150,3000))
        root = tree.AddRoot("Polyglot")
        
        #Vocab section
        vocab = tree.InsertItem(root,0,"Vocab")
        adjectives = tree.InsertItem(vocab,0,"Adjectives")
        Nouns = tree.InsertItem(vocab,1,"Nouns")
        #Verbs Section
        verbs = tree.InsertItem(root,1,"Verbs")
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.changeContent(),tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.changeContent(),tree)
    
    #Event Handler for TreeItem select
    def changeContent(self):
        print("COol beans it worked.")
        

        

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="PolyGlot",
                          size=(640,480)) 
        
        menuBar = wx.MenuBar()
        fileBtn = wx.Menu()
        exitItem = fileBtn.Append(wx.ID_FILE1, 'Select File')
        menuBar.Append(fileBtn,"File")
        self.SetMenuBar(menuBar)
        
        gridPanel = GridPanel(self, size=wx.Size(715,1000), pos=wx.Point(150,0))
        treePanel = TreePanel(self, size=wx.Size(250,1800), pos= wx.Point(0,0))
        langPan = langPanel(self,gridPanel)        
        
        #Maybe access through frame.gridPanel.grid and re display-words???

      
app = wx.App()
frame = TestFrame()
frame.Show()
app.MainLoop()


