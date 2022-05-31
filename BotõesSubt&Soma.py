# impotar a biblioteca
from tkinter import *

# Definições de comandos
def sub():
    if label1['text'] != -10:
        label1['text'] -= 1
    else:
        pass

def soma():
    if label1['text'] != 10:
        label1['text'] += 1
    else:
        pass

# janela
janela = Tk()
janela.geometry('300x200+790+270')

# Tamanho linhas
janela.grid_rowconfigure(0, weight=1)

# Tamanho colunas
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

# widgets
bt1 = Button(janela, text='-', font='Arial 26', command=sub, bg='#177b8a', fg='#e4f3f5')
bt2 = Button(janela, text='+', font='Arial 26', command=soma, bg='#177b8a', fg='#e4f3f5')
label1 = Label(janela, text=0, font='Arial 26', bg='#168e9e', fg='#e4f3f5')

# layout
bt1.grid(row=0, column=0, sticky=NSEW)
label1.grid(row=0, column=1, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)

# execução
janela.mainloop()