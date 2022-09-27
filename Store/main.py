from tkinter import*
from Cadastro import janela_cadastro
from Deletar import deletar_produto
from VerProdutos import ver_produtos

root_main = Tk()
root_main.title('INTERFACE COMERCIAL')
root_main.geometry('381x360')
root_main['bg'] = '#F0F8FF'

btn_windowC = Button(root_main, text='Cadastrar\nMercadoria', command = janela_cadastro, height=6, font='verdana 12 bold')
btn_windowC.place(x=10, y=10)

btn_windowD = Button(root_main, text='Deletar\nMercadoria', command = deletar_produto, height=6, font='verdana 12 bold')
btn_windowD.place(x=130, y=10)

btn_windowVU = Button(root_main, text='Listar\nProdutos', command = ver_produtos, height=6, width=10, font='verdana 12 bold')
btn_windowVU.place(x=250, y=10)

root_main.mainloop()