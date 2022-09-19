from tkinter import*
from Cadastro import janela_cadastro
from Deletar import deletar_produto
from VerProdutos import ver_produtos

root_main = Tk()
root_main.title('INTERFACE COMERCIAL')
root_main.geometry('640x360')
root_main['bg'] = 'orange'

btn_windowC = Button(root_main, text='Cadastrar Mercadoria', command = janela_cadastro)
btn_windowC.place(x=10, y=10)

btn_windowD = Button(root_main, text='Deletar Mercadoria', command = deletar_produto)
btn_windowD.place(x=140, y=10)

btn_windowVU = Button(root_main, text='Lista de Produtos', command = ver_produtos)
btn_windowVU.place(x=258, y=10)

root_main.mainloop()