import wx
import MySQLdb
from Menu import *
from db_conn import DBConn
import  cStringIO


   
class VentanaMenu(wx.Frame):

    #title = "About this program"

    def __init__(self,db_user, db_pass):
        Frame = wx.MiniFrame(None, -1, 'SISTEMA ALUMNOS.py', size=(450, 425),style= wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX| wx.SYSTEM_MENU | wx.CAPTION |  wx.CLOSE_BOX)
        menu(Frame,-1,db_user, db_pass)
        Frame.Show()

        
class iniciarSesion(wx.Panel):
    
    def imagenes(self,imagen,x,y):
        # pick a .jpg file you have in the working folder
        imageFile = imagen
        data = open(imageFile, "rb").read()
        # convert to a data stream
        stream = cStringIO.StringIO(data)
        # convert to a bitmap
        bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
        # show the bitmap, (5, 5) are upper left corner coordinates
        wx.StaticBitmap(self, -1, bmp, (x, y))


    def LogIn(self,event):
        self.db_user = self.USER.GetValue()
        self.db_pass = self.PASSWORD.GetValue()
        self.db_host = "localhost"
        self.db_name = "sistema_alumno"
        self.db=DBConn(self.db_host, self.db_user, self.db_pass,self.db_name)
        #Conectando al servidor y base de datos localhost
    
        #Intentamos conectarnos con el servidor
        
        try:
            
            conector=self.db.conectar()
            VentanaMenu(self.db_user,self.db_pass)
            self.db_user = self.USER.SetValue("")
            self.db_pass = self.PASSWORD.SetValue("") 
        except:
            
            wx.MessageBox("\nNo se ha podido establecer coneccion con el servidor.\n")
            self.db_user = self.USER.SetValue("")
            self.db_pass = self.PASSWORD.SetValue("") 

    def __init__(self, parent, id):
        # cracion del panel
        wx.Panel.__init__(self, parent, id)
        

        #label y texbox de usuario
        self.USER = wx.StaticText(self, -1, "USUARIO", pos = (60,90))
        self.USER = wx.TextCtrl(self, -1, "", pos = (180,90), size =(100,20))
        self.USER.SetBackgroundColour("white")

        #label y textbox de contrasena
        self.PASSWORD = wx.StaticText(self, -1, "CONTRASEÑA", pos = (60, 120))
        self.PASSWORD = wx.TextCtrl(self, -1, "",style=wx.TE_PASSWORD, pos = (180, 120), size =(100,20))
        self.PASSWORD.SetBackgroundColour("white")

        #Boton De LOGIN
        Login = wx.Button(self, -1, 'LOGIN', pos=(165, 200), size = (100,50))
        self.Bind(wx.EVT_BUTTON, self.LogIn, id=Login.GetId())

        #imagen='Picture1.png'
        #self.imagenes(imagen,2,0)
        
# creamos una clase donde se deriva el modulo wx.App
class Main(wx.App):

    # wxWindows llama a este metodo para ser inicializado
    def OnInit(self):
        
        #crear los objetos de la clase MyFrame
        frame = wx.Frame(None, -1, 'LogIn.py', size=(400, 425),style= wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX| wx.SYSTEM_MENU | wx.CAPTION |  wx.CLOSE_BOX)

        iniciarSesion(frame,-1)
        frame.Centre()
        frame.Show()

        # WxWindows entonces identificara esta como nuestra ventana principal
        self.SetTopWindow(frame)

        # regresa verdadero cuando esta bien
        return True

app = Main(0)     # Crea una instancia de la aplicacion cronometor
app.MainLoop()     # hace la ejecucion del widget y lo deja en espera
