import sqlite3 
import tkinter as ttk
from tkinter import *
from tkinter import messagebox
import customtkinter

class Pañol:
    #db_name = False

    def __init__(self, ventana_herramienta):
        self.window = ventana_herramienta
        self.window.title("Aplicacion del pañol")
        self.window.geometry("1350x700")
        self.window.resizable(0,0)
        self.window.config(bd=10)


        #### TITULO ####
        titulo = Label(ventana_herramienta, text="REGISTRO DE HERRAMIENTAS", fg="black", font=("helvetica", 17, "bold"), pady=10)
        titulo.pack()


        #### FRAME MARCO ESTUDIANTE####
        marco = LabelFrame(ventana_herramienta, text="Datos del Estudiante", font=("helvetica", 20, "bold"), pady=5)
        marco.config(bd=2)
        marco.pack()

        #### Formulario DATOS####
        lbl_nombre_apellido = Label(marco, text="Nombre y Apellido", font=("helvetica", 15, "bold"))
        lbl_nombre_apellido.grid(row=1, column=0, sticky="s", pady=5, padx=8)

        nombre_apellido = Entry(marco, width=40)
        nombre_apellido.grid(row=1, column=1, pady=5, padx=100)

        lbl_profesor = Label(marco, text="Profesor", font=("helvetica", 15, "bold"))
        lbl_profesor.grid(row=2, column=0, sticky="s", pady=5, padx=8)

        profesor = Entry(marco, width=40)
        profesor.grid(row=2, column=1, pady=5, padx=100)

        lbl_curso = Label(marco, text="Curso", font=("helvetica", 15, "bold"))
        lbl_curso.grid(row=3, column=0, pady=5, padx=8)

        curso = Entry(marco, width=40)
        curso.grid(row=3, column=1)

        ### MARCO HERRAMIENTAS ###
        marco_herramientas = LabelFrame(ventana_herramienta, text="Herramientas a llevar",font=("helvetica", 20, "bold"),pady=5)
        marco_herramientas.config(bd=2)
        marco_herramientas.pack(pady=20, padx=200)


        lbl_herramientas = Label(marco_herramientas, text="Herramientas", font=("helvetica", 15, "bold"))
        lbl_herramientas.grid(row=1, column=0, pady=5, padx=8)

        herramientas =  customtkinter.CTkTextbox(marco_herramientas)
        herramientas.grid(row=1, column=3) 



app = ttk.Tk()

my_app = Pañol(app)
app.mainloop()