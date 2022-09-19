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
        en_ver.insert(END, 'ID:        NOME:       PREÇO/C:       PREÇO/V:\n')
        for i in range(0, tm):
            en_ver.insert(END, f'{lista[i][0]}      {lista[i][1]}       {lista[i][2]}             {lista[i][3]}\n')

    #CONFIGURAÇÕES DA JANELA DE CADASTRO
    janela_vu = Toplevel()
    janela_vu.title('Deletar Produtos')
    janela_vu.geometry('540x292')
    janela_vu['bg'] = 'orange'

    lbl_nome = Label(janela_vu, text='VER LISTA DE PRODUTOS CADASTRADOS', font='Congenial 14 bold', bg='orange')
    lbl_nome.place(x=60, y=26)

    en_ver = Text(janela_vu, width=46, height=12, font='Congenial 10')
    en_ver.place(x=19, y=60)

    btn0 = Button(janela_vu, text='LISTAR PRODUTOS', width=16, height=0, font='Congenial 10 bold', command = ver)
    btn0.place(x=360, y=120)

    btn_destroy = Button(janela_vu, text='VOLTAR', width=10, height=0, font='Congenial 10 bold', command = janela_vu.destroy)
    btn_destroy.place(x=360, y=160)

    janela_vu.mainloop()
    
    cursor.close()
    conexao.close()