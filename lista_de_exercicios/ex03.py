# Faça um Programa que peça o nome e a idade de uma pessoa e mostre
nome = input("Digite seu nome: ")
idade = (input("Digite sua idade: "))

if nome and idade:
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é', nome[::-1])
    print (f'Seu nome tem {len(nome)} letras')
    print(f'Seu nome contem ou não espaços: {" " in nome}')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
      print("Nome ou idade não fornecidos.")
  


