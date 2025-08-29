#Aprendendo um pouco sonre a função input()
#O input() sempre retorna uma string
#Se você quiser trabalhar com números, é necessário converter(TypeCast) da string para o tipo numérico desejado (int ou float)
numero_1 = input("Digite o primeiro número: ")
numero_2 = input("Digite o segundo número: ")
print(f"A soma dos números é: {(numero_1 + numero_2)}")
#O resultado acima não é o esperado, pois o input() retorna uma string
print('--' * 10)
#Para corrigir isso, precisamos converter as entradas para int ou float
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
print(f"A soma dos números é: {(numero_1 + numero_2)}")
#Agora o resultado é o esperado, pois as entradas foram convertidas para int

