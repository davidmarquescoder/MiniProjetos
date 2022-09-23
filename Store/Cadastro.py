from cgitb import text
from sqlite3 import Cursor
from turtle import width
from unicodedata import name
import mysql.connector
from tkinter import*

def janela_cadastro():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = None,
        database = 'basestore',
    )
    cursor = conexao.cursor()

    #CREAT
    def cadastrar():
        name = en_nome.get()
        pc = en_preco1.get()
        pv = en_preco2.get()
        qt = en_quantidade.get()
        comando_cadastro = f'INSERT INTO cadastroprodutos (nome_produtos, preco_compra, preco_venda, quantidade_produtos) VALUES ("{str(name).upper()}", "{float(pc)}", "{float(pv)}", "{int(qt)}")'
        cursor.execute(comando_cadastro)
        conexao.commit()
        caixaT.insert(END, f'STATUS: ITEM CADASTRADO\n\n\nÚLTIMO ITEM CADASTARDO:\n{name}')

    #CONFIGURAÇÕES DA JANELA DE CADASTRO
    janela_c = Toplevel()
    janela_c.title('Cadastrar Produtos')
    janela_c.geometry('650x280')
    janela_c['bg'] = 'orange'

    lbl_nome = Label(janela_c, text='NOME PRODUTO', font='Congenial 14 bold', bg='orange')
    lbl_nome.place(x=10, y=30)

    lbl_preco1 = Label(janela_c, text='PREÇO DE COMPRA', font='Congenial 14 bold', bg='orange')
    lbl_preco1.place(x=10, y=60)

    lbl_preco2 = Label(janela_c, text='PREÇO DE VENDA', font='Congenial 14 bold', bg='orange')
    lbl_preco2.place(x=10, y=90)

    lbl_quantidade = Label(janela_c, text='QUANTIDADE', font='Congenial 14 bold', bg='orange')
    lbl_quantidade.place(x=10, y=120)

    en_nome = Entry(janela_c, width=14)
    en_nome.place(x=240, y=34)

    en_preco1 = Entry(janela_c, width=14)
    en_preco1.place(x=240, y=64)

    en_preco2 = Entry(janela_c, width=14)
    en_preco2.place(x=240, y=98)

    en_quantidade = Entry(janela_c, width=14)
    en_quantidade.place(x=240, y=132)

    caixaT = Text(janela_c, width=34, height=10)
    caixaT.place(x=350, y=20)

    btn0 = Button(janela_c, text='CADASTRAR', width=11, font='Congenial 12 bold', command = cadastrar)
    btn0.place(x=200, y=200)

    btn_destroy = Button(janela_c, text='VOLTAR', width=11, font='Congenial 12 bold', command = janela_c.destroy)
    btn_destroy.place(x=40, y=200)

    janela_c.mainloop()
    
    cursor.close()
    conexao.close()