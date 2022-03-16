import wx
import wx.grid
from utils import loadPickle, dumpPickle, displayWords, numLangs
import plyglt


def displayGrid(root):

    gridPanel = wx.Panel(root, size=wx.Size(1000,1000), pos=wx.Point(150,0))
    grid = wx.grid.Grid(gridPanel,size=wx.Size(1000,1000))
    grid.CreateGrid(1000 ,numLangs + 3)
    grid.SetDefaultCellBackgroundColour(wx.Colour(255,255,255))
    grid.SetDefaultCellOverflow(False)
    grid.SetDefaultCellFont(wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_MEDIUM))
    dic = loadPickle("words.txt")
    displayWords(grid, dic)
    grid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, plyglt.TestFrame.OnChangeCell)
    
    return grid


def displayTree():
    pass

def displayRHS():
    pass

