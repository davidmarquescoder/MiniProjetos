#Utilizando o Firebase como banco de dados para esse projeto
import requests

pessoas = requests.get('https://basedados1-67a0c-default-rtdb.firebaseio.com/.json')
pessoas = pessoas.json()
p1 = pessoas[1]['Nome']
p2 = pessoas[1]['Idade']
p3 = pessoas[1]['Sobrenome']
print(p1,p2,p3)