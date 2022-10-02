from tkinter import *
import tkinter
import time 
import random
import pyautogui

ventana=Tk()

ventana.title("Spameador")
ventana.resizable(True,True)
ventana.iconbitmap("E:\Programación\icono.ico")
ventana.geometry("500x300")


cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()
          
etiqueta      =  tkinter.Label(ventana) 
etiqueta.pack()
def textoDeLaCaja():
   text20 = cajaTexto.get()
   etiqueta["text"] = text20
           
boton1 = tkinter.Button(ventana, text = "click", command = textoDeLaCaja ) 
boton1.pack()

ventana.mainloop()


