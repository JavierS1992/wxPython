# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:42:27 2018

@author: JavIer
"""
import wx

import glob #buscar un determinado tipo de archivos
import os
del app

class ventana_padre(wx.Frame):
    def __init__(self,parent,title,num,cont):
        wx.Frame.__init__(self,parent=parent,title=title,size=(400,200))
        sz=wx.BoxSizer(wx.VERTICAL)
        self.cont=cont
        self.Refresh()
        
        panel=wx.Panel(self,-1)
        
        self.texto=wx.StaticText(panel,-1)
        boton=wx.Button(panel,-1,"Ventana Hija")
        
        self.texto.SetLabel(str(self.cont))
        
        sz.Add(boton,1,wx.EXPAND)
        sz.Add(self.texto,1,wx.EXPAND)
        
        self.Bind(wx.EVT_BUTTON,self.Llamar)
        
        panel.SetSizer(sz)
        self.Centre(True)
        self.Show()
        
    def Llamar(self,event):
        self.cont=self.cont+1
        ventana2=ventana_hija(None,"Ventana Hija",0,self.cont)
        self.Destroy()
    

class ventana_hija(wx.Frame):
    def __init__(self,parent,title,num,cont):
        wx.Frame.__init__(self,parent=parent,title=title,size=(200,200))
        sz=wx.BoxSizer(wx.VERTICAL)
        self.cont=cont
        
        panel=wx.Panel(self,-1)
        btnr=wx.Button(panel,-1,"Regresar")
        texto=wx.StaticText(panel,-1)
        texto.SetLabel(str(self.cont))

        sz.Add(texto,1,wx.EXPAND)        
        sz.Add(btnr,1,wx.EXPAND)
        
        self.Bind(wx.EVT_BUTTON,self.Regresar)
        
        panel.SetSizer(sz)
        self.Centre(True)
        self.Show()
        self.num=cont
        
    def Regresar(self,event):
        frame=ventana_padre(None,"Ventana Padre",0,self.cont)
        frame.Show() 
        self.Destroy()
        
        

        
if __name__=='__main__':
    app=wx.App()
    frame=ventana_padre(None,"Ventana Padre",0,0)
    app.MainLoop()

    
    
