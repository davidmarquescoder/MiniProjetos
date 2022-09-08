import requests
import json

cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #Fazendo a requisição das informações
cotacao = cotacao.json() #Transformando as informações formato JSON
cotacao_dolar = cotacao['USDBRL']['bid'] #Buscando os valores dentro da lista
cotacao_dolar = float(cotacao_dolar) #Transformando de str para float

print(f'DOLAR: {cotacao_dolar:.2f}') #Imprimindo a cotação do  dolar