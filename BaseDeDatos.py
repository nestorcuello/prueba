import wx
import MySQLdb

from Tabla_Alumnos import *


# creamos una clase donde se deriva el modulo wx.App
class Main(wx.App):

    # wxWindows llama a este metodo para ser inicializado
    def OnInit(self):
        
        #crear los objetos de la clase MyFrame
        frame = wx.MiniFrame(None, -1, 'SISTEMA ALUMNOS.py', size=(900, 425),style= wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX| wx.SYSTEM_MENU | wx.CAPTION |  wx.CLOSE_BOX)

        Tabla_Alum(frame,-1)
        
        frame.Centre()
        frame.Show()

        # WxWindows entonces identificara esta como nuestra ventana principal
        self.SetTopWindow(frame)

        # regresa verdadero cuando esta bien
        return True

app = Main(0)     # Crea una instancia de la aplicacion cronometor
app.MainLoop()     # hace la ejecucion del widget y lo deja en espera
