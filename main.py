from tkinter import *
from tkinter import ttk

cor_visor = '#3c7782'
cor_cinza_claro = '#ced5d9'
cor_amarela = '#f7d17e'
cor_branca = '#fafbfc'


#criação de janela e configurações de nome e tamanho
janela = Tk()
janela.title('Calculadora')
janela.geometry("240x340")

#define o frame superior = tela da calculadora
frame_superior = Frame(janela, width=240, height=80, bg=cor_visor)
frame_superior.grid(row=0, column=0)

#define o frame inferior = botões da calculadora
frame_inferior = Frame(janela, width=240, height=260)
frame_inferior.grid(row=1, column=0)

todos_valores = ''


def entrada_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)


def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

valor_texto = StringVar()

#labels
app_label = Label(frame_superior, textvariable=valor_texto, width=16, height=3, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor_visor, fg=cor_branca)
app_label.place(x=0, y=0)


#botões
#linha1
button1 = Button(frame_inferior, command=limpar_tela, text='C', width=11, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button1.place(x=0, y=0)
button2 = Button(frame_inferior, command=lambda: entrada_valores('%'), text='%', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button2.place(x=120, y=0)
button3 = Button(frame_inferior, command=lambda: entrada_valores('/'), text='/', width=5, height=2, bg=cor_amarela, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button3.place(x=180, y=0)

#linha2
button4 = Button(frame_inferior, command=lambda: entrada_valores('7'), text='7', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button4.place(x=0, y=52)
button5 = Button(frame_inferior, command=lambda: entrada_valores('8'), text='8', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button5.place(x=60, y=52)
button6 = Button(frame_inferior, command=lambda: entrada_valores('9'), text='9', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button6.place(x=120, y=52)
button7 = Button(frame_inferior, command=lambda: entrada_valores('*'), text='*', width=5, height=2, bg=cor_amarela, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button7.place(x=180, y=52)

#linha3
button8 = Button(frame_inferior, command=lambda: entrada_valores('4'), text='4', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button8.place(x=0, y=104)
button9 = Button(frame_inferior, command=lambda: entrada_valores('5'), text='5', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button9.place(x=60, y=104)
button10 = Button(frame_inferior, command=lambda: entrada_valores('6'), text='6', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button10.place(x=120, y=104)
button11 = Button(frame_inferior, command=lambda: entrada_valores('-'), text='-', width=5, height=2, bg=cor_amarela, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button11.place(x=180, y=104)

#linha4
button12 = Button(frame_inferior, command=lambda: entrada_valores('1'), text='1', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button12.place(x=0, y=156)
button13 = Button(frame_inferior, command=lambda: entrada_valores('2'), text='2', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button13.place(x=60, y=156)
button14 = Button(frame_inferior, command=lambda: entrada_valores('3'), text='3', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button14.place(x=120, y=156)
button15 = Button(frame_inferior, command=lambda: entrada_valores('+'), text='+', width=5, height=2, bg=cor_amarela, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button15.place(x=180, y=156)

#linha5
button16 = Button(frame_inferior, command=lambda: entrada_valores('0'), text='0', width=11, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button16.place(x=0, y=208)
button17 = Button(frame_inferior, command=lambda: entrada_valores('.'), text='.', width=5, height=2, bg=cor_cinza_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button17.place(x=120, y=208)
button18 = Button(frame_inferior, command=calcular, text='=', width=5, height=2, bg=cor_amarela, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button18.place(x=180, y=208)


janela.mainloop()
