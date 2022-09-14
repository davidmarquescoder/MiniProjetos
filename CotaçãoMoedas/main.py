import requests
from tkinter import*

def dolar():
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #Fazendo a requisição das informações
    cotacao = cotacao.json() #Transformando as informações formato JSON

    cotacao_dolar = cotacao['USDBRL']['bid'] #Buscando os valores dentro da lista
    cotacao_dolar = float(cotacao_dolar) #Transformando de str para float

    valores  = f'DOLAR   R$ {cotacao_dolar:.2f}' #Imprimindo a cotação das moedas
    lbl_dolar['text'] = valores

def euro():
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #Fazendo a requisição das informações
    cotacao = cotacao.json() #Transformando as informações formato JSON

    cotacao_euro = cotacao['EURBRL']['bid'] #Buscando os valores dentro da lista
    cotacao_euro = float(cotacao_euro) #Transformando de str para float

    valores  = f'EURO   R$ {cotacao_euro:.2f}' #Imprimindo a cotação das moedas
    lbl_euro['text'] = valores

def bitcoin():
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #Fazendo a requisição das informações
    cotacao = cotacao.json() #Transformando as informações formato JSON

    cotacao_bitcoin = cotacao['BTCBRL']['bid'] #Buscando os valores dentro da lista
    cotacao_bitcoin = float(cotacao_bitcoin) #Transformando de str para float

    valores  = f'BITCOIN   R$ {cotacao_bitcoin:.2f}' #Imprimindo a cotação das moedas
    lbl_bitcoin['text'] = valores

def limpar():
    lbl_dolar['text'] = ''
    lbl_euro['text'] = ''
    lbl_bitcoin['text'] = ''

#INTERFACE
janela = Tk()
janela.title('Cotacoin Base')
janela.geometry('640x360')
janela['bg'] = '#D3D3D3'

btn_dolar = Button(janela, text='DOLAR (USD)', command = dolar, bd=2, relief=RIDGE)
btn_dolar.place(x=30, y=30)

btn_euro = Button(janela, text='EURO (EUR)', command = euro, bd=2, relief=RIDGE)
btn_euro.place(x=120, y=30)

btn_bitcoin = Button(janela, text='BITCOIN (BTC)', command = bitcoin, bd=2, relief=RIDGE)
btn_bitcoin.place(x=200, y=30)

btn_limpar = Button(janela, text='LIMPAR', command = limpar, bd=2, relief=RIDGE)
btn_limpar.place(x=295, y=30)

lbl_dolar = Label(janela, text='', bg= '#D3D3D3', font='verdana 9')
lbl_dolar.place(x=30, y=60)

lbl_euro = Label(janela, text='', bg= '#D3D3D3', font='verdana 9')
lbl_euro.place(x=30, y=78)

lbl_bitcoin = Label(janela, text='', bg= '#D3D3D3', font='verdana 9')
lbl_bitcoin.place(x=30, y=98)

janela.mainloop()