from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import tkinter as tk

class Frame(tk.Frame):
    
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Tkinter")
        self.ventana.configure(background='#FFFFFF')
        self.ventana.geometry('1550x640')
        self.ventana.mainloop()

aplicacion1=Frame()