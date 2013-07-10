import  cStringIO

class Image():    
    def __init__():
        Imagen=''
        
    def imagenes(self):
        # pick a .jpg file you have in the working folder
        imageFile = 'header.png'
        data = open(imageFile, "rb").read()
        # convert to a data stream
        stream = cStringIO.StringIO(data)
        # convert to a bitmap
        bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
        # show the bitmap, (5, 5) are upper left corner coordinates
        wx.StaticBitmap(self, -1, bmp, (0, 0))

        # pick a .jpg file you have in the working folder
        imageFile = 'Gobierno.png'
        data = open(imageFile, "rb").read()
        # convert to a data stream
        stream = cStringIO.StringIO(data)
        # convert to a bitmap
        bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
        # show the bitmap, (5, 5) are upper left corner coordinates
        wx.StaticBitmap(self, -1, bmp, (0, 400))
