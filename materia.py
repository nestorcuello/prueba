import wx
import MySQLdb

class Tabla_Mat(wx.Panel):


    def Consulta_Clave(self,event): 
        Clave= self.Clave.GetValue()
        #table =self.table
        busqueda ="SELECT * FROM materias WHERE clave = '%s'" % (Clave)
        #self.buscar(Clave,table)
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
                Clave = str(row[0])
                Nombre_mat =str(row[1])
                #Impresion de los datos en los campos
                self.Clave.SetValue("%s\n" % (Clave))
                self.Nombre_mat.SetValue("%s\n" % (Nombre_mat))

            

        except:
            print "error"

    def Actualizar(self,event):
        
        #Preparamos la consulta sql para modificar los datos de la tabla alumnos,
        #donde el numero de carnet sea igual al ingresado por el usuario anteriormente.
        cursor = self.referencia.cursor()
        #table = self.table
        Al_Clave= self.Clave.GetValue()
        Al_Nombre_mat= self.Nombre_mat.GetValue()
 
        sql = "UPDATE materias SET clave = '%s', nombre_mat = '%s' WHERE Clave = '%s' " %(Al_Clave, Al_Nombre_mat,Al_Clave) 
        try:
            #Ejecutamos
            cursor.execute(sql)
            #Guardamos
            self.referencia.commit()
            self.Limpiar()
        except:
            self.referencia.rollback()       
        
    def Altas(self,event):
        cursor=self.referencia.cursor()
        Al_Clave= self.Clave.GetValue()
        Al_Nombre_mat= self.Nombre_mat.GetValue()
        
        
        sql='insert into materias (clave, nombre_mat) values ("' + Al_Clave +'" , "' + Al_Nombre_mat +'")'
        try:
            cursor.execute(sql)
            cursor.close()
            self.referencia.commit()
            self.Limpiar()
        except:
            cursor.rollback()

    def borrar(self,event):
        
        Clave= self.Clave.GetValue()
        cursor=self.referencia.cursor()

        sql = "DELETE FROM materias WHERE clave = '%s'" % Clave
        try:
            cursor.execute(sql)
            cursor.close()
            self.referencia.commit()
            limpiar()
        except:
            self.referencia.rollback()
    def Limpiar(self):
        #Impresion de los datos en los campos
        self.Clave.SetValue("")
        self.Nombre_mat.SetValue("")
    
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
        self.SetBackgroundColour("Blue")
        self.referencia = self.variables (usuario,contra)
        titulo = wx.StaticText(self, -1, 'Materias', (190, 15))
        titulo_font = titulo.GetFont()
        titulo_font.SetWeight(wx.BOLD)
        titulo.SetFont(titulo_font)

        wx.StaticLine(self, -1, (30, 70), (340,5))

        #label y texbox de Numero De Control
        self.Clave = wx.StaticText(self, -1, "Clave", pos = (50,100))
        self.Clave = wx.TextCtrl(self, -1, "", pos = (50, 120), size =(100,20))
        self.Clave.SetBackgroundColour("white")

        #label y texbox de Paterno
        self.Nombre_mat = wx.StaticText(self, -1, "Nombre de la Materia", pos = (230,100))
        self.Nombre_mat = wx.TextCtrl(self, -1, "", pos = (230, 120), size =(100,20))
        self.Nombre_mat.SetBackgroundColour("white")

        wx.StaticLine(self, -1, (30, 170), (340,5))

        #Boton De Consulta
        Boton = wx.Button(self, -1, 'CONSULTA', pos=(30,180), size = (100,30))
        self.Bind(wx.EVT_BUTTON, self.Consulta_Clave, id=Boton.GetId())

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
