import math
import requests
from tkinter import *
import os




janela = Tk()
janela.title('Calculadora tangente')

img_fundo = PhotoImage(file='fundo.png')
img_botao = PhotoImage(file='botao.png')

label_fundo = Label(janela, image=img_fundo)
label_fundo.pack()

#label_botao = Label(janela, image=img_botao)
#label_botao.pack()

def bt_click():
    print('bt_click')
    if (str(ed1.get()).isnumeric()):

        n1= int(ed1.get())
        #n2= int(ed2.get())

        lb["text"] = lb["text"] = float(math.tan(math.radians(n1)))

    else:
        lb['text']= 'Valores informados inválidos.'

ed1=Entry(janela)
ed1.place(width=210,height=31,x=95, y=104)

bt=Button(janela, bd=0, image=img_botao, command=bt_click)
bt.place (width=92,height=32,x=155, y=163)

lb = Label(janela, text='')
lb.place(width=179, height=26, x=110,y=218)

#texto1 = Label(janela, text='Digite seu angulo em graus')
#texto1.place (x=90, y=60)

janela.geometry('400x300+200+200')
janela.mainloop()


#lb["text"] = math.ceil(float(math.tan(math.radians(n1))))
#and str(ed2.get()).isnumeric()