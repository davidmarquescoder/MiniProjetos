import os

chances = 3
secreto  = 'ferrari'
digitadas = []

while True:
    if chances <= 0:
        print('Você perdeu! suas chances acabaram =(')
        break

    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('AHHH! ISSO NÃO VALE, DIGITE SOMENTE UMA LETRA POR VEZ!')
        continue
    if letra.isnumeric():
        print('AHHH! ISSO NÃO VALE, DIGITE APENAS LETRAS!!!')
        continue
    if letra in digitadas:
        print('Essa letra já foi digitada!')
        continue
    
    digitadas.append(letra)
    
    if letra in secreto:
        print(f'UHULL! A LETRA "{letra}" EXISTE NA PALAVRA!\n')
    else:
        print(f'A LETRA "{letra}" NÃO EXISTE NA PALAVRA!\n')
        chances -= 1
        digitadas.pop()
    
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else: 
            secreto_temp += '*'
    
    if secreto_temp == secreto:
        print(f'VOCÊ GANHOU!! A PALAVRA SECRETA É: {secreto_temp}')
        break
    
    os.system('pause')
    os.system('cls')
    print(f'PALAVRA: {secreto_temp}\n\n')