from tkinter import*
from Cadastro import janela_cadastro
from Deletar import deletar_produto
from VerProdutos import ver_produtos

root_main = Tk()
root_main.title('INTERFACE COMERCIAL')
root_main.geometry('381x300')
root_main['bg'] = '#F0F8FF'

btn_windowC = Button(root_main, text='CADASTRAR\nMERCADORIA', command = janela_cadastro, height=6,  width=17, font='berlim 12 bold', bg='#B0C4DE', fg='black')
btn_windowC.place(x=5, y=10)

btn_windowD = Button(root_main, text='DELETAR\nMERCADORIA', command = deletar_produto, height=6, width=17, font='berlim 12 bold', bg='#B0C4DE', fg='black')
btn_windowD.place(x=195, y=10)

btn_windowVU = Button(root_main, text='LISTAR\nPRODUTOS', command = ver_produtos, height=6, width=34, font='berlim 12 bold', bg='#B0C4DE', fg='black')
btn_windowVU.place(x=15, y=150)

root_main.mainloop()