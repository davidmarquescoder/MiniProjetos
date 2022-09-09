#Utilizando o Firebase como banco de dados para esse projeto
import requests

def cadastrar():
    login = '{"Nome": "Lucas"}'
    pessoas = requests.post('https://basedados1-67a0c-default-rtdb.firebaseio.com/.json', data=login)
    pessoas = pessoas.json()
    print(pessoas)

def atualizar():
    login = '{"Nome": "David"}'
    pessoas = requests.patch('https://basedados1-67a0c-default-rtdb.firebaseio.com/-NBYcVl8BK_ZcoJE6WKP.json', data=login)
    pessoas = pessoas.json()
    print(pessoas)