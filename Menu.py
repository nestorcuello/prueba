import wx
from Tabla_Alumnos import *
from carrera import Tabla_Carrera
from materia import Tabla_Mat
from gridBitacora import BaseD

class FrameAlumnos(wx.Frame):
    title = 'Settings'
    def __init__(self,x,y):
        marco=wx.Frame.__init__(self, wx.GetApp().TopWindow, title=self.title, size=(x, y), style=(wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN))
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.MakeModal()
               

    #----------------------------------------------------------------------
    def onClose(self, event):
        """
        Make the frame non-modal as it closes to re-enable other windows
        """
        self.MakeModal(False)
        self.Destroy()
        
class menu(wx.Panel):
        def evento1(self,e):
                frame=FrameAlumnos(900,350)
                Tabla_Alum(frame,-1,self.db_user, self.db_pass)
                frame.Show()
                
                
        def evento2(self,e):
                frame=FrameAlumnos(450,350)
                Tabla_Carrera(frame,-1,self.db_user, self.db_pass)
                frame.Show()
                
        def evento3(self,e):
                frame=FrameAlumnos(400,350)
                Tabla_Mat(frame,-1,self.db_user, self.db_pass)
                frame.Show()
        def evento4(self,e):
            frame=FrameAlumnos(600,600)
            BaseD(frame,-1)
            frame.Show()
                
        def __init__(self, parent, id,db_user, db_pass):
            # cracion del panel
            wx.Panel.__init__(self, parent, id)
            self.db_user=db_user
            self.db_pass=db_pass
            
            #USUARIO CONECTADO
            self.USUARIO = wx.StaticText(self, -1, "USUARIO:  "+self.db_user, pos = ( 350,10))

            #BOTONES
            Alumno  = wx.Button(self, -1, 'Alumnos', pos=(20, 70), size = (100,50))
            Materia = wx.Button(self, -1, 'Materia', pos=(20, 140), size = (100,50))
            Carrera = wx.Button(self, -1, 'Carrera', pos=(20, 210), size = (100,50))

            #LIGAS DE EVENTOS A BOTONES
            self.Bind(wx.EVT_BUTTON, self.evento1, id=Alumno.GetId())
            self.Bind(wx.EVT_BUTTON, self.evento2, id=Carrera.GetId())
            self.Bind(wx.EVT_BUTTON, self.evento3, id=Materia.GetId())

            if(self.db_user == "root"):
                Bitacora = wx.Button(self, -1, 'BITACORA', pos=(250, 70), size = (100,50))
                self.Bind(wx.EVT_BUTTON, self.evento4, id=Bitacora.GetId())
                

        
            

            

