#Bibliotecas
from tkinter import*
import datetime
import pandas as pd
#FIM DO BLOCO BIBLIOTECAS

#Importação dos Módulos
from Leonardo import abrir_leo
from Larissa import abrir_lari
from Amanda import abrir_aman
from Gustavo import abrir_gust
from Josiane import abrir_josi
from Luciana import abrir_luci
from Lucas import abrir_luc
#FIM DO BLOCO DE MÓDULOS

def criate_table():
    data = datetime.date.today()

    TabelaBase = pd.read_excel('Tabela_base.xlsx')
    TabelaBase.to_excel(f'Registros {data}.xlsx', index = False)


'''INTERFACE
CONFIGURAÇÕES DA JANELA (INTERFACE)
'''
janela_main = Tk()
janela_main.geometry('435x120+800+100')
janela_main.title('CHECKPOINT ASSOCIADOS')
janela_main['bg'] = 'gray'

btn1 = Button(text='Leonardo', command= abrir_leo)
btn1.place(x=10, y=30)

btn2 = Button(text='Larissa', command= abrir_lari)
btn2.place(x=80, y=30)

btn3 = Button(text='Amanda', command= abrir_aman)
btn3.place(x=135, y=30)

btn4 = Button(text='Gustavo', command= abrir_gust)
btn4.place(x=200, y=30)

btn5 = Button(text='Josiane', command= abrir_josi)
btn5.place(x=263, y=30)

btn6 = Button(text='Luciana', command= abrir_luci)
btn6.place(x=322, y=30)

btn7 = Button(text='Lucas', command= abrir_luc)
btn7.place(x=384, y=30)

btn_table = Button(text='GERAR TABELA', command= criate_table, bg='light green')
btn_table.place(x=334, y=80)

janela_main.mainloop()