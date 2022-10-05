from tkinter import*
import pandas as pd
import datetime

def registrar_saida():
    data = datetime.date.today()
    hora = datetime.datetime.now()

    tabela = pd.read_excel(f'Registros {data}.xlsx')
    tabela.loc[0, 'DATA'] = data
    tabela.loc[0, 'SAIDA'] = hora
    tabela.loc[0, 'NOME'] = 'LEONARDO'

    tabela.to_excel(f'Registros {data}.xlsx', index = False)

def registrar_retorno():
    data = datetime.date.today()
    hora = datetime.datetime.now()
    tabela = pd.read_excel(f'Registros {data}.xlsx')
    tabela.loc[0, 'RETORNO'] = hora
    
    tabela.to_excel(f'Registros {data}.xlsx', index = False)

def abrir_leo():
    janela_leo = Toplevel()
    janela_leo.geometry('200x200+800+100')
    janela_leo.title('Registro de horário')

    btn_saida = Button(janela_leo, text='SAÍDA', command= registrar_saida)
    btn_saida.place(x=10, y=30)

    btn_entrada = Button(janela_leo, text='RETORNO', command= registrar_retorno)
    btn_entrada.place(x=10, y=80)

    janela_leo.mainloop()