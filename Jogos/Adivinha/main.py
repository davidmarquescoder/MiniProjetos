from objetos import*
import random
import os

a = random.choice([0, 1, 2, 3])
secreto  = [ob[a].lower(), dc[a].upper()]
digitadas = []

os.system('cls')
print('======ADIVINHA======')
print('Mecânica do Game:\n1 - Tente adivinhar a palavra secreta\n2 - Só vale digitar uma letra por vez até desvendar a palavra secreta e ganhar o game!\n3 - Você pode escolher entre 3 modos de game (easy, medium, hard)\n\n\n')

os.system('pause')
os.system('cls')

print('======MODO DE JOGO======\nEasy - 6 chances para acertar as letras\nMedium - 3 chances para acertar as letras\nHard - 1 chance para acertar as letras\n\n')
while True:
    modo = (input('Escolha o modo de jogo: '))
    os.system('cls')

    if modo == 'easy':
        chances = 6
        break
    elif modo == 'medium':
        chances = 3
        break
    elif modo == 'hard':
        chances = 1
        break
    elif modo != 'easy' and modo != 'medium' and modo != 'hard':
        print('Digite um modo de jogo válido!!\n\n'.upper())
        continue
print('======O JOGO COMEÇOU======\n\n')
while True:
    if chances <= 0:
        print('Você perdeu! suas chances acabaram =(')
        os.system('pause')
        break

    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('AHHH! ISSO NÃO VALE, DIGITE SOMENTE UMA LETRA POR VEZ!')
        continue
    if letra.isnumeric():
        print('AHHH! ISSO NÃO VALE, DIGITE APENAS LETRAS!!!')
        continue
    if letra in digitadas:
        os.system('cls')
        print('\n\nEssa letra já foi digitada!\n\n'.upper())
        os.system('pause')
        continue
    
    digitadas.append(letra)
    
    if letra in secreto[0]:
        print(f'UHULL! A LETRA "{letra}" EXISTE NA PALAVRA!\n')
    else:
        print(f'A LETRA "{letra}" NÃO EXISTE NA PALAVRA!\n')
        chances -= 1
        if chances == 0:
            os.system('cls')
            print(f'Chances = {chances}\n')
            print('O jogo acabou pra você!\nSuas chances acabaram =(\n\n')
            os.system('pause')
            break
        print(f'Você perdeu uma de suas chances, agora você tem apenas {chances} chances\n\n'.upper())
        dica = input('Você quer uma dica? ')
        if dica == 'sim':
            print(secreto[1])
        digitadas.pop()
    
    secreto_temp = ''
    for letra_secreta in secreto[0]:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else: 
            secreto_temp += '*'
    
    if secreto_temp == secreto[0]:
        print(f'VOCÊ GANHOU!! A PALAVRA SECRETA É: {secreto_temp}')
        os.system('pause')
        break
    
    os.system('pause')
    os.system('cls')
    print(f'PALAVRA: {secreto_temp}\n\n')