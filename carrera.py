import wx
import MySQLdb

class Tabla_Carrera(wx.Panel):


    def Consulta_Carrera(self,event): 
        NumCarrera = self.NoCar.GetValue()
        #table =self.table
        busqueda ="SELECT * FROM carrera WHERE No_Carrera = '%s'" % (NumCarrera)
        #self.buscar(No_car,table)
        try:
            
            cursor = self.referencia.cursor()
            cursor.execute(busqueda)
        except:
            
            print "error en ejecucion"
            #Preprarmos la consulta para mostrar todos los registros de la tabla Alumnos donde el nombre sea igual al ingresado por el usuario.
            
        
        try:
             
            results = cursor.fetchall()
        
            for row in results:
                
                #Asignacion de Datos
                NoCar = str(row[0])
                Nombre =str(row[1])
                #Impresion de los datos en los campos
                self.NoCar.SetValue("%s\n" % (NoCar))
                self.Nombre.SetValue("%s\n" % (Nombre))

        except:
            print "error"

    def Actualizar(self,event):
        
        #Preparamos la consulta sql para modificar los datos de la tabla alumnos,
        #donde el numero de carnet sea igual al ingresado por el usuario anteriormente.
        cursor = self.referencia.cursor()
        #table = self.table
        Al_NoCar= self.NoCar.GetValue()
        Al_Nombre= self.Nombre.GetValue()
 
        sql = "UPDATE carrera SET No_Carrera = '%s', Nombre = '%s' WHERE No_Carrera = '%s' " %(Al_NoCar, Al_Nombre,Al_NoCar) 
        try:
            #Ejecutamos
            cursor.execute(sql)
            #Guardamos
            self.referencia.commit()
        except:
            self.referencia.rollback()       
        
    def Altas(self,event):
        cursor=self.referencia.cursor()
        Al_NoCar= self.NoCar.GetValue()
        Al_Nombre= self.Nombre.GetValue()
        
        
        sql='insert into carrera (No_Carrera, Nombre) values ("' + Al_NoCar +'" , "' + Al_Nombre +'")'
        try:
            cursor.execute(sql)
            cursor.close()
            self.referencia.commit()
            self.Limpiar()
        except:
            self.referencia.rollback()

    def borrar(self,event):
        
        NoCar= self.NoCar.GetValue()
        cursor=self.referencia.cursor()

        sql = "DELETE FROM carrera WHERE No_Carrera = '%s'" % NoCar
        try:
            cursor.execute(sql)
            cursor.close()
            self.referencia.commit()
            limpiar()
        except:
            cursor.rollback()
    def Limpiar(self):
        #Impresion de los datos en los campos
        self.NoCar.SetValue("")
        self.Nombre.SetValue("")
    
    def clrCampos(self,event):
        self.Limpiar()

    def variables (self,usuario,contra):
        self.host='localhost'
        self.user='root'
        self.passw='amairani26'
        self.database='sistema_alumno'
        self.referencia=' '
        self.table = ''
        return MySQLdb.connect(self.host, self.user, self.passw, self.database)
    
    
    def __init__(self, parent, id,usuario,contra):

        # cracion del panel
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("Red")
        self.referencia = self.variables(usuario,contra)
        titulo = wx.StaticText(self, -1, 'Carrera', (190, 15))
        titulo_font = titulo.GetFont()
        titulo_font.SetWeight(wx.BOLD)
        titulo.SetFont(titulo_font)

        wx.StaticLine(self, -1, (30, 70), (340,5))

        #label y texbox de Numero De Control
        self.Clave = wx.StaticText(self, -1, "Clave de la Carrea", pos = (50,100))
        self.NoCar = wx.TextCtrl(self, -1, "", pos = (50, 120), size =(100,20))
        self.Clave.SetBackgroundColour("white")

        #label y texbox de Paterno
        self.Nombre_mat = wx.StaticText(self, -1, "Nombre de la Carrea", pos = (230,100))
        self.Nombre = wx.TextCtrl(self, -1, "", pos = (230, 120), size =(100,20))
        self.Nombre_mat.SetBackgroundColour("white")

        wx.StaticLine(self, -1, (30, 170), (340,5))

        #Boton De Consulta
        Boton = wx.Button(self, -1, 'CONSULTA', pos=(30,180), size = (100,30))
        self.Bind(wx.EVT_BUTTON, self.Consulta_Carrera, id=Boton.GetId())

        #Boton De ACTUALIZACION
        Boton = wx.Button(self, -1, 'ACTUALIZACIONES', pos=(150,180), size = (100,30))
        self.Bind(wx.EVT_BUTTON, self.Actualizar, id=Boton.GetId())

        #Boton De BORRAR REGISTRO
        Boton = wx.Button(self, -1, 'BORRAR\nREGISTRO', pos=(270,180), size = (100,30))
        self.Bind(wx.EVT_BUTTON, self.borrar, id=Boton.GetId())

        #Boton De Altas
        Boton = wx.Button(self, -1, 'ALTAS', pos=(100,250), size = (100,30))
        self.Bind(wx.EVT_BUTTON, self.Altas, id=Boton.GetId())

        #Boton De Limpiar Casillas
        Boton = wx.Button(self, -1, 'LIMPIAR\nCAMPOS', pos=(240,250), size = (100,30))
        self.Bind(wx.EVT_BUTTON, self.clrCampos, id=Boton.GetId())



# creamos una clase donde se deriva el modulo wx.App
#class MainAlu(wx.App):

     #wxWindows llama a este metodo para ser inicializado
 #   def OnInit(self):
        
        #crear los objetos de la clase MyFrame
  #      frame = wx.MiniFrame(None, -1, 'Materias.py', size=(400, 425),style= wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX| wx.SYSTEM_MENU | wx.CAPTION |  wx.CLOSE_BOX)

   #     Tabla_Carrera(frame,-1)
    #    frame.Centre()
     #   frame.Show()

        #WxWindows entonces identificara esta como nuestra ventana principal
      #  self.SetTopWindow(frame)

        # regresa verdadero cuando esta bien
       # return True

#app = MainAlu(0)     # Crea una instancia de la aplicacion cronometor
#app.MainLoop()     # hace la ejecucion del widget y lo deja en espera
