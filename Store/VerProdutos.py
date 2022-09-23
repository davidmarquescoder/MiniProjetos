from sqlite3 import Cursor
import mysql.connector
from tkinter import*

def ver_produtos():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = None,
        database = 'basestore',
    )
    cursor = conexao.cursor()

    #CREAT
    def ver():
        comando_ver = 'SELECT * FROM basestore.cadastroprodutos;'
        cursor.execute(comando_ver)
        lista = cursor.fetchall()
        tm = len(lista)
        for i in range(0, tm):
            en_ver0.insert(END, f'{lista[i][0]}\n')
            en_ver1.insert(END, f'{lista[i][1]}\n')
            en_ver2.insert(END, f'{lista[i][3]}\n')
            en_ver3.insert(END, f'{lista[i][4]}\n')

    #CONFIGURAÇÕES DA JANELA DE CADASTRO
    janela_vu = Toplevel()
    janela_vu.title('Deletar Produtos')
    janela_vu.geometry('540x292')
    janela_vu['bg'] = 'orange'

    lbl_nome = Label(janela_vu, text='VER LISTA DE PRODUTOS CADASTRADOS', font='Congenial 14 bold', bg='orange')
    lbl_nome.place(x=60, y=15)

    lbl_des0 = Label(janela_vu, text='ID', bg='orange')
    lbl_des0.place(x=48, y=48)

    lbl_des1 = Label(janela_vu, text='NOME', bg='orange')
    lbl_des1.place(x=117, y=48)

    lbl_des2 = Label(janela_vu, text='PREÇO/V', bg='orange')
    lbl_des2.place(x=188, y=48)

    lbl_des3 = Label(janela_vu, text='QUANT', bg='orange')
    lbl_des3.place(x=272, y=48)

    en_ver0 = Text(janela_vu, width=10, height=12, font='Congenial 10')
    en_ver0.place(x=20, y=70)

    en_ver1 = Text(janela_vu, width=10, height=12, font='Congenial 10')
    en_ver1.place(x=99, y=70)

    en_ver2 = Text(janela_vu, width=10, height=12, font='Congenial 10')
    en_ver2.place(x=178, y=70)

    en_ver3 = Text(janela_vu, width=10, height=12, font='Congenial 10')
    en_ver3.place(x=257, y=70)

    btn0 = Button(janela_vu, text='LISTAR PRODUTOS', width=16, height=0, font='Congenial 10 bold', command = ver)
    btn0.place(x=368, y=120)

    btn_destroy = Button(janela_vu, text='VOLTAR', width=10, height=0, font='Congenial 10 bold', command = janela_vu.destroy)
    btn_destroy.place(x=368, y=160)

    janela_vu.mainloop()
    
    cursor.close()
    conexao.close()