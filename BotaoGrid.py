# impotar a biblioteca
from tkinter import *

# janela
janela = Tk()

# Tamanho linhas
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)

# Tamanho colunas
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

# widgets
bt1 = Button(janela, text='Bt 1', font='Arial 26')
bt2 = Button(janela, text='Bt 2', font='Arial 26')
bt3 = Button(janela, text='Bt 3', font='Arial 26')
bt4 = Button(janela, text='Bt 4', font='Arial 26')
bt5 = Button(janela, text='Bt 5', font='Arial 26')
bt6 = Button(janela, text='Bt 6', font='Arial 26')

# layout
bt1.grid(row=0, column=0, sticky=NSEW)
bt2.grid(row=0, column=1, sticky=NSEW)
bt3.grid(row=0, column=2, sticky=NSEW)
bt4.grid(row=1, column=0, sticky=NSEW)
bt5.grid(row=1, column=1, sticky=NSEW)
bt6.grid(row=1, column=2, sticky=NSEW)

# execução
janela.mainloop()