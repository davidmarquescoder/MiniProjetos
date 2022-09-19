from sqlite3 import Cursor
import mysql.connector
from tkinter import*

def deletar_produto():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = None,
        database = 'basestore',
    )
    cursor = conexao.cursor()

    #CREAT
    def deletar():
        name = en_nome.get()
        comando_delet = f'DELETE FROM cadastroprodutos WHERE nome_produtos = "{name}"'
        cursor.execute(comando_delet)
        conexao.commit()

    #CONFIGURAÇÕES DA JANELA DE CADASTRO
    janela_d = Toplevel()
    janela_d.title('Deletar Produtos')
    janela_d.geometry('540x260')
    janela_d['bg'] = 'orange'

    lbl_nome = Label(janela_d, text='DIGITE O NOME DO PRODUTO QUE DESEJA DELETAR', font='Congenial 14 bold', bg='orange')
    lbl_nome.place(x=12, y=30)

    en_nome = Entry(janela_d, width=30, font='Congenial 14')
    en_nome.place(x=98, y=100)

    btn0 = Button(janela_d, text='DELETAR PRODUTO', width=16, height=0, font='Congenial 10 bold', command = deletar)
    btn0.place(x=260, y=180)

    btn_destroy = Button(janela_d, text='VOLTAR', width=10, height=0, font='Congenial 10 bold', command = janela_d.destroy)
    btn_destroy.place(x=140, y=180)

    janela_d.mainloop()
    
    cursor.close()
    conexao.close()