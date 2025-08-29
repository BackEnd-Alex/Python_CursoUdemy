# Exercicio para treinar if, elif e else, e operadores de comapração.
# Faça um programa que peça dois números inteiros e imprima o maior deles.
num1 = input('Digite o primeiro valor:')
num2 = input('Digite o segundo valor:')

if num1 > num2:
    print(f'O num1 {num1} é maior que o num2 {num2}')
elif num2 > num1:
    print(f'O num2 {num2} é maior que o num1 {num1}')
else:
    print('Os dois números são iguais')