# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:01:16 2020

@author: cruov
"""

import tkinter as tk
from tkinter import Tk, Label, Button
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image
from wavefront import wavefront
import datetime

class GUI:
    def __init__(self,master):
        self.master=master
        self.master.title("SISTEMA AÉREO AUTÓNOMO PARA EL MONITOREO DE GANADO")
        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight() 
        canvas1 = tk.Canvas(root, width = w, height = h, bg = 'white', relief = 'raised')
        canvas1.pack()
        guinda_ipn='#6D1A42'
        azul_ipn='#353554'
        self.t1 = tk.Label(text=" ",width=w,height=3, bg=guinda_ipn, fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(0, 0, window=self.t1)
        
        self.img = ImageTk.PhotoImage(Image.open("ipn.PNG").resize((65,70))) 
        canvas1.create_image(w//10,h//20, anchor='nw', image=self.img)
        self.img2 = ImageTk.PhotoImage(Image.open("cr_robotics.PNG").resize((112,70))) 
        canvas1.create_image(w//2-56,h//20, anchor='nw', image=self.img2)
        self.img3 = ImageTk.PhotoImage(Image.open("upiita.PNG").resize((70,70))) 
        canvas1.create_image(w*9//10-70,h//20, anchor='nw', image=self.img3)
        self.img4 = ImageTk.PhotoImage(Image.open("Mapa.PNG").resize((450,252))) 
        canvas1.create_image(w*6//10,h*4//20, anchor='nw', image=self.img4)
        self.img5 = ImageTk.PhotoImage(Image.open("tabla.PNG").resize((450,252))) 
        canvas1.create_image(w*6//10,h*11//20, anchor='nw', image=self.img5)
        self.img6 = ImageTk.PhotoImage(Image.open("dron.PNG").resize((450,252))) 
        canvas1.create_image(w*1//10,h*11//20, anchor='nw', image=self.img6)
              
        self.b1 = tk.Button(text=" Conectar dron ",width=18,height=1, command=self.conectar_dron, bg=guinda_ipn, fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*2//10, h*4//20, window=self.b1)
        self.b2 = tk.Button(text=" Definir ruta ", width=18,height=1,command=self.ingresar_ruta, bg=guinda_ipn, fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*2//10, h*5//20, window=self.b2)
        self.b3 = tk.Button(text=" Registrar nueva vaca ", width=18,height=1,command=self.ingresar_ruta, bg=guinda_ipn, fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*2//10, h*6//20, window=self.b3)
        self.b4 = tk.Button(text=" Mostrar registros ", width=18,height=1,command=self.ingresar_ruta, bg=guinda_ipn, fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*2//10, h*7//20, window=self.b4)
        
        
        
        self.b6 = tk.Button(text=" Comenzar recorrido ", width=18,height=1,command=self.ingresar_ruta, bg='green', fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*4//10, h*5//20, window=self.b6)
        self.b7 = tk.Button(text=" Detener misión ", width=18,height=1,command=self.ingresar_ruta, bg='red', fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*4//10, h*6//20, window=self.b7)
        self.b8 = tk.Button(text=" Cerrar ", width=18,height=1,command=self.ingresar_ruta, bg=guinda_ipn, fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*4//10, h*7//20, window=self.b8)
        
        self.t1 = tk.Label(text=" Estado: Dron no conectado ",width=22,height=1, bg=azul_ipn, fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*4//10+20, h*4//20, window=self.t1)
        self.t2 = tk.Label(text=datetime.date.today().ctime(),width=22,height=1, bg=azul_ipn, fg='white', font=('Montserrat', 12, 'bold'))
        canvas1.create_window(w*4//10, h*18//20, window=self.t2)

#                              .resize((128,70)))         
    def conectar_dron(self):
        MessageBox.showerror("Atención", "Dron no conectado o ruta no establecida") # título, mensaje

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