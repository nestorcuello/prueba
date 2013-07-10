import wx
import wx.grid
import MySQLdb
from operator import itemgetter, attrgetter

class GenericTable(wx.grid.PyGridTableBase):
    def __init__(self, data, rowLabels=None, colLabels=None):
        wx.grid.PyGridTableBase.__init__(self)
        self.data = data
        self.rowLabels = rowLabels
        self.colLabels = colLabels
        
    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])  

    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]
        
    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]
        
    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        pass         
                   
class SimpleGrid(wx.grid.Grid):
    
    def __init__(self, parent,data,rowLabels,colLabels):
        wx.grid.Grid.__init__(self, parent, -1, pos=(70,100), size =(475,300))
        tableBase = GenericTable(data,colLabels,rowLabels)
        self.SetTable(tableBase)
        
class BaseD(wx.Panel):
    def __init__(self, parent, id):
        self.host='localhost'
        self.user='root'
        self.passwd='amairani26'
        self.db='sistema_alumno'
        self.referencia=' '
        self.table = 'bitacora'
        self.referencia = MySQLdb.connect(self.host, self.user, self.passwd, self.db)
        self.data = []
    
        wx.Panel.__init__(self, parent, id)

        self.SetClientSize(wx.Size(384, 447))
        self.SetBackgroundColour("grey")
        
        self.staticText2 = wx.StaticText(self, -1, label='BITACORA', pos=(50, 10), size=wx.Size(137, 23), style=0)
        self.staticText2.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Comic Sans MS'))
     
        self.OnBuscarButton()        
       
    
    def OnBuscarButton(self):

        cursor = self.referencia.cursor()
        e=cursor.execute("SELECT Usuario,Movimiento,Tabla,Registro,Fecha from bitacora") 
        self.data = cursor.fetchall()

        colLabels = ("USUARIO","MOVIMIENTO","TABLA","REGISTRO","FECHA")
        rowLabels = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                     "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
        grid = SimpleGrid(self,self.data,colLabels,rowLabels)                         
                           
