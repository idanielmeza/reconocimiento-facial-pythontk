from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from db import run_query
import cv2
import uuid
import imutils

class Registro:
    def __init__(self):
        self.ventana = Toplevel()
        self.ventana.title("Registra un usuario")

        Label(self.ventana, text="Nombre: ").grid(row=0, column=0)
        self.nombre = Entry(self.ventana)
        self.nombre.grid(row=0, column=1)

        self.labelVideo = Label(self.ventana)
        self.labelVideo.grid(row=1, column=0, columnspan=2)


        ttk.Button(self.ventana, text='Tomar Foto', command= self.guardar).grid(row=2, column=1)
        self.captura()


    ##captura de la imagen
    def captura(self):
        self.video = cv2.VideoCapture(0)
        self.iniciar()
    
    def iniciar(self):
        ret, frame = self.video.read()
        if ret == True:
            frame = imutils.resize(frame, width=400)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.labelVideo.configure(image=imgtk)
            self.labelVideo.image = imgtk
            self.ventana.after(10, self.iniciar)
    
    def guardar(self):
        ret, frame = self.video.read()
        if ret:
            img_name = uuid.uuid4()
            cv2.imwrite(f"images/{img_name}.jpg", frame)
            run_query("INSERT INTO users(nombre,image) VALUES(?, ?)", (self.nombre.get(), f'{img_name}.jpg'))
            self.video.release()
            messagebox.showinfo("Guardado", "Usuario guardado")
            self.ventana.destroy()
        

       

