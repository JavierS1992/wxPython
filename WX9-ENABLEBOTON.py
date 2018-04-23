# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:33:20 2018

@author: JavIer
"""

import wx

import glob #buscar un determinado tipo de archivos
import os


class RadioB(wx.Frame):
    def __init__(self,parent,title,num):
        wx.Frame.__init__(self,parent=parent,title=title,size=(400,200))
        sz=wx.BoxSizer(wx.HORIZONTAL)
        self.i=0
        #Boton
        self.b1=wx.Button(self,-1,"Uno")      
        self.b2=wx.Button(self,-1,"Dos")
        
        sz.Add(self.b1,1,wx.EXPAND|wx.ALL,2)
        sz.Add(self.b2,1,wx.EXPAND|wx.ALL,2)
        
        self.Bind(wx.EVT_BUTTON,self.Bloquear,self.b1)
        self.Bind(wx.EVT_BUTTON,self.Bloquear2,self.b2)
               
        
        self.SetSizer(sz)
        self.Centre(True)
        self.Show()
        
    def Bloquear(self,event):
        if self.i==0:
            self.b2.Disable()
        else:
            if self.i==5:
                self.b2.Enable()
                self.b1.Disable()
                self.i=-1
        self.i=self.i+1
    
    def Bloquear2(self,event):
        self.b2.Disable()
        self.b1.Enable()
   

        
if __name__=='__main__':
    app=wx.App()
    frame=RadioB(None,"Boton Enable",0)
    app.MainLoop()
    del app