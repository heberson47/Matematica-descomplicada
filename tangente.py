import math
import requests
from tkinter import *




janela = Tk()
janela.title('Calculadora tangente')


def bt_click():
    print('bt_click')
    if (str(ed1.get()).isnumeric()):

        n1= int(ed1.get())
        #n2= int(ed2.get())

        lb["text"] = lb["text"] = float(math.tan(math.radians(n1)))

    else:
        lb['text']= 'Valores informados inválidos.'

ed1=Entry(janela)
ed1.place(x=100, y=100)
#ed2=Entry(janela)
#ed2.place(x=100, y=130)

bt=Button(janela, text='Resultado', width=20, command=bt_click)
bt.place (x=100, y= 150)

lb = Label(janela, text='')
lb.place(x=100,y=200)

texto1 = Label(janela, text='Digite seu angulo em graus')
texto1.place (x=90, y=60)

janela.geometry('400x300+200+200')
janela.mainloop()


#lb["text"] = math.ceil(float(math.tan(math.radians(n1))))
#and str(ed2.get()).isnumeric()