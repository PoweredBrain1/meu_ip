#Meu IP por Nuno Alves
import socket
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Meu IP Versão 0.2 de Nuno Barata Alves")

h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
nome = "O nome deste computador é: " + h_name
ip = "O endereço IP deste computador é: " + IP_addres


def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)

def nome1():
    label1.config(text=nome)
    label1.after(1000,nome1)

def ip1():
    label2.config(text=ip)
    label2.after(1000,ip1)

label = Label(root, font=("arial", 20), background = "white", foreground = "green")
label1 = Label(root, font=("arial", 20), background = "white", foreground = "green")
label2 = Label(root, font=("arial", 20), background = "white", foreground = "green")
label1.pack(anchor='center')
label2.pack(anchor='center')
label.pack(anchor='center')


nome1()
ip1()
time()


mainloop()