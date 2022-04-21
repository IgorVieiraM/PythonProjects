"""
É necessário a instalação dos pacotes gtts e playsound

"""

from gtts import gTTS
from playsound import playsound
from tkinter import Tk
from tkinter import font
from tkinter import Label
from tkinter import Entry
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import Button
from tkinter import messagebox
from tkinter import W
import os

class Speaker:
    def __init__(self):
        self.linguagens = ("pt", "en", "es", "fr")
        self.velocidade = ("Normal","Lento")
        self.window()
        self.copyright()

    def window(self):

        self.root = Tk()
        self.root.title("Speaker")
        self.root.geometry("240x300+500+200")
        self.root.resizable(False, False)
        self.root.option_add('*Dialog.msg.font', 'Arial 20')

        self.varLinguagem = StringVar(self.root)
        self.varLinguagem.set(self.linguagens[0])

        self.varVelocidade = StringVar(self.root)
        self.varVelocidade.set(self.velocidade[0])

        fonteTitulo = font.Font(family='Helvetica', size=16, weight='bold')
        fonte = font.Font(family="Arial", size=8, weight='bold')

        self.label0 = Label(self.root, text="Speaker", font=fonteTitulo)
        self.label0.grid(column=0, row=0, pady=20, padx=0,columnspan=2)

        self.label1 = Label(self.root, text="texto: ", font=fonte)
        self.label1.grid(column=0, row=1, padx=0, pady=0)

        self.label2 = Label(self.root, text="linguagem: ", font=fonte)
        self.label2.grid(column=0, row=2, pady=0, padx=0)

        self.label3 = Label(self.root, text="Velocidade: ", font=fonte)
        self.label3.grid(column=0, row=3, pady=0, padx=0)

        self.entry1 = Entry(self.root, width=20)
        self.entry1.grid(column=1, row=1, padx=6, pady=10, sticky=W)

        self.opt1 = OptionMenu(self.root, self.varLinguagem, *self.linguagens)
        self.opt1.grid(column=1, row=2, padx=5, pady=10, sticky=W)
        self.opt1.config(width=14)

        self.opt2 = OptionMenu(self.root, self.varVelocidade, *self.velocidade)
        self.opt2.grid(column=1, row=3, padx=5, pady=10, sticky=W)
        self.opt2.config(width=14)

        self.buttonEnviar = Button(self.root, width=16, height=2, text='Enviar', font=fonteTitulo,command=self.play)
        self.buttonEnviar.grid(column=0, row=4, padx=10, pady=10, columnspan=2)

        self.root.mainloop()

    def play(self):

        self.texto = (self.entry1.get())
        self.audio = 'speech.mp3'

        try:
            if (self.varVelocidade.get() == "Normal"):
                self.sp = gTTS(text=self.texto, lang=self.varLinguagem.get(), slow=False)
                self.sp.save(self.audio)
                playsound(self.audio)

            else:
                self.sp = gTTS(text=self.texto, lang=self.varLinguagem.get(), slow=True)
                self.sp.save(self.audio)
                playsound(self.audio)

        except AssertionError:
            messagebox.showerror("Falha ao localizar texto", "Digite um texto para prosseguir!")

        if os.path.isfile('./speech.mp3'):
            os.remove("speech.mp3")

    def copyright(self):
        messagebox.showinfo("Speaker","Desenvolvido por: Igor Vieira\nContato:igor.vieira.ivm@gmail.com")

Speaker()