"""nome = 'Alexsandro'
tamanho_nome = len(nome)
print(nome)

indice = 0
novo_nome = ''  

while indice < len(nome):
    letra = nome [indice]  
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)    """

#Calculadora com while
while True:
    num1 = input('Digite o primeiro número: ') # todo inpunt retorna uma string
    num2 = input('Digite o segundo número: ')
    operacao = input('Digite a operação (+ - * / ): ')
    numeros_validos = None

    try:
    
        float(num1) # tenta converter string para float
        float(num2)
        numeros_validos = True

    except:
      
      numeros_validos = None

    if numeros_validos is None: 
        print('Um ou ambos os números digitados são inválidos.')
        continue
    if operacao not in '+-*/':
        print('Operação inválida.')
        continue
    if len(operacao) > 1:
        print('Digite apenas uma operação.')
        continue
    if operacao == '+':
        soma =  float(num1) + float(num2)
        print(f'Soma = {soma:.2f}')
    elif operacao == '-':
        subtracao = float(num1) - float(num2)
        print(f'Subtração = {subtracao:.2f}')
    elif operacao == '*':
        multiplicacao = float(num1) * float(num2)
        print(f'Multiplicação = {multiplicacao:.2f}')
    elif operacao == '/':
        if num2 == '0':
            print('Não é possível dividir por zero.')
            continue
        divisao = float(num1) / float(num2)
        print(f'Divisão = {divisao:.2f}')
        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

