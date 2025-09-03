"""Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero inteiro: ')
try:
    #converte string para inteiro
    numero = int(numero)
    if numero % 2 == 0:
        print('O numero é par')
    else:
     print(f'O numero é impar')

except ValueError:
    print('Isso não é um numero inteiro')

print('-'*20)
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são? ')
#
try:
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom dia 0 -11')
    elif 12 <= hora <= 17:
        print('Boa tarde 12 - 17')
    elif 18 <= hora <= 23:
        print('Boa noite 18 - 23')
    else:
        print('Isso não é uma hora valida')
except ValueError:
        print('Isso não é uma hora valida')
print('-'*20)
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Qual o seu nome? ')
try:
     if len(nome) <= 4:
            print('Seu nome é curto')
     elif len(nome)<=6:
            print('Seu nome é normal')
     else:
            print('Seu nome é muito grande')
except ValueError:
    print('Isso não é um nome valido')            