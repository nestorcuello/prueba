import wx
import MySQLdb
from db_conn import DBConn
class Tabla_Alum(wx.Panel):


    def Consulta_NumControl(self,event): 
        Control= self.Num_Control.GetValue()
        #table =self.table
        busqueda ="SELECT * FROM alumno WHERE No_Cont = '%s'" % (Control)
        #self.buscar(Control,table)
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
                Control = str(row[0])
                Nombre =str(row[1])
                Materno = str(row[2])
                Paterno = str( row[3] )
                Telefono = str(row[4])
                Correo = str(row[5])
                #Impresion de los datos en los campos
                self.Num_Control.SetValue("%s\n" % (Control))
                self.NOMBRE.SetValue("%s\n" % (Nombre))
                self.Materno.SetValue("%s\n" % (Materno))
                self.Paterno.SetValue("%s\n" % (Paterno))
                self.Telefono.SetValue("%s\n" % (Telefono))
                self.Correo.SetValue("%s\n"%(Correo)) 

        except:
            print "error"

    def Actualizar(self,event):
        
        #Preparamos la consulta sql para modificar los datos de la tabla alumnos,
        #donde el numero de carnet sea igual al ingresado por el usuario anteriormente.
        cursor = self.referencia.cursor()
        #table = self.table
        Al_NcontrolA= self.Num_Control.GetValue()
        Al_apellidopA= self.NOMBRE.GetValue()
        Al_apellidomA=self.Materno.GetValue()
        Al_NombreA=self.Paterno.GetValue()
        Al_direccionA= self.Telefono.GetValue()
        Al_telefonoA=self.Correo.GetValue()
 
        sql = "UPDATE alumno SET No_Cont = '%s', nombre = '%s', Materno= '%s', Paterno= '%s',Telefono='%s',Correo='%s' WHERE No_Cont = '%s' " %(Al_NcontrolA,Al_apellidopA,Al_apellidomA,Al_NombreA,Al_direccionA,Al_telefonoA,Al_NcontrolA) 
        try:
            #Ejecutamos
            cursor.execute(sql)
            #Guardamos
            self.referencia.commit()
        except:
            self.referencia.rollback()       
        
    def Altas(self,event):
        cursor=self.referencia.cursor()
        Al_NcontrolA= self.Num_Control.GetValue()
        Al_apellidopA= self.NOMBRE.GetValue()
        Al_apellidomA=self.Materno.GetValue()
        Al_NombreA=self.Paterno.GetValue()
        Al_direccionA= self.Telefono.GetValue()
        Al_telefonoA=self.Correo.GetValue()
        
        
        sql='insert into alumno (No_Cont,nombre,Materno,Paterno,Telefono,Correo) values ("' + Al_NcontrolA +'" , "' + Al_apellidopA +'" , "' + Al_apellidomA +'", "' + Al_NombreA +'", "' + Al_direccionA +'", "' + Al_telefonoA +'")'
        try:
            cursor.execute(sql)
            cursor.close()
            self.referencia.commit()
            self.Limpiar()
        except:
            cursor.rollback()

    def borrar(self,event):
        
        Control= self.Num_Control.GetValue()
        cursor=self.referencia.cursor()

        sql = "DELETE FROM alumno WHERE No_Cont = '%s'" % Control
        try:
            cursor.execute(sql)
            cursor.close()
            self.referencia.commit()
            limpiar()
        except:
            cursor.rollback()
    def Limpiar(self):
        #Impresion de los datos en los campos
        self.Num_Control.SetValue("")
        self.NOMBRE.SetValue("")
        self.Materno.SetValue("")
        self.Paterno.SetValue("")
        self.Telefono.SetValue("")
        self.Correo.SetValue("")
    
    def clrCampos(self,event):
        self.Limpiar()

    def variables (self,usuario,contra):
        self.host='localhost'
        self.user=usuario#'root'
        self.passw=contra#'amairani26'
        self.database='sistema_alumno'
        self.referencia=' '
        self.table = ''
        return MySQLdb.connect(self.host, self.user, self.passw, self.database)
    
            
    def __init__(self,parent, id,usuario,contra):

        # cracion del panel
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("yellow")

        self.referencia = self.variables(usuario,contra)
        #self.crearEstructura()
        
        titulo = wx.StaticText(self, -1, 'BASE DE DATOS', (375, 15))
        titulo_font = titulo.GetFont()
        titulo_font.SetWeight(wx.BOLD)
        titulo.SetFont(titulo_font)

        wx.StaticLine(self, -1, (30, 70), (850,5))

        #label y texbox de Numero De Control
        self.Num_Control = wx.StaticText(self, -1, "Numero de Control", pos = (60,100))
        self.Num_Control = wx.TextCtrl(self, -1, "", pos = (60, 120), size =(100,20))
        self.Num_Control.SetBackgroundColour("white")

        #label y texbox de Paterno
        self.NOMBRE = wx.StaticText(self, -1, "Nombre", pos = (200,100))
        self.NOMBRE = wx.TextCtrl(self, -1, "", pos = (180, 120), size =(100,20))
        self.NOMBRE.SetBackgroundColour("white")

        #label y texbox de Materno
        self.Materno = wx.StaticText(self, -1, "Apellido Materno", pos = (300,100))
        self.Materno = wx.TextCtrl(self, -1, "", pos = (290, 120), size =(100,20))
        self.Materno.SetBackgroundColour("white")

        #label y texbox de Nombre
        self.Paterno = wx.StaticText(self, -1, "Apellido Paterno", pos = (425,100))
        self.Paterno = wx.TextCtrl(self, -1, "", pos = (400, 120), size =(100,20))
        self.Paterno.SetBackgroundColour("white")
        
        #label y texbox de Direccion
        self.Telefono = wx.StaticText(self, -1, "Telefono", pos = (535,100))
        self.Telefono = wx.TextCtrl(self, -1, "", pos = (510, 120), size =(100,20))
        self.Telefono.SetBackgroundColour("white")
    
        #label y texbox de Ciudad
        self.Correo = wx.StaticText(self, -1, "Correo", pos = (670,100))
        self.Correo = wx.TextCtrl(self, -1, "", pos = (650, 120), size =(100,20))
        self.Correo.SetBackgroundColour("white")

        wx.StaticLine(self, -1, (30, 170), (850,5))

        #Boton De Consulta
        Boton = wx.Button(self, -1, 'CONSULTA', pos=(150,180), size = (100,50))
        self.Bind(wx.EVT_BUTTON, self.Consulta_NumControl, id=Boton.GetId())

        #Boton De ACTUALIZACIONES
        Boton = wx.Button(self, -1, 'ACTUALIZACIONES', pos=(300,180), size = (100,50))
        self.Bind(wx.EVT_BUTTON, self.Actualizar, id=Boton.GetId())

        #Boton De BORRAR REGISTRO
        Boton = wx.Button(self, -1, 'BORRAR\nREGISTRO', pos=(450,180), size = (100,50))
        self.Bind(wx.EVT_BUTTON, self.borrar, id=Boton.GetId())

        #Boton De Altas
        Boton = wx.Button(self, -1, 'ALTAS', pos=(600,180), size = (100,50))
        self.Bind(wx.EVT_BUTTON, self.Altas, id=Boton.GetId())

        #Boton De Limpiar Casillas
        Boton = wx.Button(self, -1, 'LIMPIAR\nCAMPOS', pos=(375,250), size = (100,50))
        self.Bind(wx.EVT_BUTTON, self.clrCampos, id=Boton.GetId())



# creamos una clase donde se deriva el modulo wx.App
#class MainAlu(wx.App):

    # wxWindows llama a este metodo para ser inicializado
 #   def OnInit(self):
        
        #crear los objetos de la clase MyFrame
  #      frame = wx.MiniFrame(None, -1, 'SISTEMA ALUMNOS.py', size=(900, 425),style= wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX| wx.SYSTEM_MENU | wx.CAPTION |  wx.CLOSE_BOX)

   #     Tabla_Alum(frame,-1)
    #    frame.Centre()
     #   frame.Show()

        #WxWindows entonces identificara esta como nuestra ventana principal
      #  self.SetTopWindow(frame)

        # regresa verdadero cuando esta bien
       # return True

#app = MainAlu(0)     # Crea una instancia de la aplicacion cronometor
#app.MainLoop()     # hace la ejecucion del widget y lo deja en espera
#        
