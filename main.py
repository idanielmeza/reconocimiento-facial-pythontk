from tkinter import ttk
from tkinter import *
import registro
import reconocimiento

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bienvenido")
        # self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="white")

        ttk.Button(text='Registro', command= self.registrar_usuario).grid(row=0, column=0)
        ttk.Button(text='Reconocimineto', command = self.reconocimiento_face).grid(row=0, column=1)


        self.root.mainloop()


    def registrar_usuario(self):
        registro.Registro()

    def reconocimiento_face(self):
        reconocimiento.Reconocimiento()

if __name__ == '__main__':
    app = Main()
    
