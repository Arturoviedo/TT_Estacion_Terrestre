# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:40:42 2020

@author: cruov
"""

import tkinter as tk
from tkinter import Tk, Label, Button
from PIL import ImageTk, Image
class GUI:
    def __init__(self,master):
        self.master=master
        self.master.title("SISTEMA AÉREO AUTÓNOMO PARA EL MONITOREO DE GANADO")
        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight() 
        
        
        master.geometry("%dx%d+0+0" % (w, h))
        root.configure(background='steelblue2')
            
        #canvas1 = tk.Canvas(root, width = w, height = h, bg = 'steelblue2', relief = 'raised')
        #canvas1.pack()
        
        self.img = ImageTk.PhotoImage(Image.open("C:/Users/cruov/OneDrive - Instituto Politecnico Nacional/UPIITA/Decimo/TT1/GUI_TT/ipn.PNG").resize((128,70))) 
        #C:/Users/cruov/OneDrive - Instituto Politecnico Nacional/UPIITA/Decimo/TT1/GUI_TT/ipn.PNG
        print(self.img)
        self.panel = Label(master, image = self.img)
        
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")
        
            
        #canvas1.create_image(h/2, w/2, anchor='nw', image=img)
        
        self.conectar_button = Button(text="      Import CSV File      ", command=self.conectar_dron, bg='green', fg='white', font=('helvetica', 12, 'bold'))
        self.conectar_button.pack()
        #canvas1.create_window(h/3, w/3, window=browseButton_CSV)

        FillButton_CSV = tk.Button(text="      Fill web site     ", command=self.ingresar_ruta, bg='green', fg='white', font=('helvetica', 12, 'bold'))
        #canvas1.create_window(150, 200, window=FillButton_CSV)

        text_window=Label(root, bg='green', text='No te equivoques')
        text_window.pack()
        #canvas1.create_window(150, 275, window=text_window)
#                              .resize((128,70)))         
        
        
    def conectar_dron(self):
        pass
    def ingresar_ruta(self):
        pass
    def iniciar_recorrido(self):
        pass
    def boton_paro(self):
        pass



        
root = tk.Tk()
my_gui=GUI(root)

root.mainloop()