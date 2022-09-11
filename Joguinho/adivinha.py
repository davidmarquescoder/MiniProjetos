secreto  = 'carro'
digitadas = []

while True:
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
    print(f'\n{digitadas}\n')
    
    if letra in secreto:
        print(f'UHULL! A LETRA "{letra}" EXISTE NA PALAVRA!\n')
        
        if len(digitadas) == len(secreto)-1:
            res = input('Você já achou todas as letras, tente adivinhar qual a palavra secreta: ')
            if res == secreto:
                print('PARABENS!!! VOCÊ ACERTOU A PALAVRA SECRETA!!!!!')
                break
            else:
                print(f'Sinto muito, mas a palavra secreta era "{secreto}"\n Você perdeu =(')
                break
    else:
        print(f'A LETRA "{letra}" NÃO EXISTE NA PALAVRA!')
        digitadas.pop()