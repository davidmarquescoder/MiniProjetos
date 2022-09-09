#Utilizando o Firebase como banco de dados para esse projeto
import requests

nome = 'david'

def cadastrar():
    login = '{"Nome": "Lucas"}'
    pessoas = requests.post('https://basedados1-67a0c-default-rtdb.firebaseio.com/.json', data=login)
    pessoas = pessoas.json()
    print(pessoas)

def atualizar():
    login = '{"Nome": "David"}'
    pessoas = requests.patch('https://basedados1-67a0c-default-rtdb.firebaseio.com/-NBYdtRwx5tmEmCO2PNV.json', data=login)
    pessoas = pessoas.json()
    print(pessoas)

def teste():
    req = requests.get('https://basedados1-67a0c-default-rtdb.firebaseio.com/.json')
    req = req.json()
    print(req)

teste()