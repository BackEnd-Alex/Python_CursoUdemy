# Operadores lógicos:
# and, or, not
# and -> todas as expressões precisam ser verdadeiras
# or -> pelo menos uma expressão precisa ser verdadeira
# not -> inverte o valor lógico
# Obs: Em python, esses operadores são  diferentes de java, que no caso são representados por &&, || e !.

entrada = input('[E]entrar [S]Sair:')
senha_digitada = input('Senha: ')
senha_permitida = '123456'
if(entrada == 'E' and senha_digitada == senha_permitida):
    print('Entrar')
else:
    print('Sair')

if 1 and 1:
        print(True and 1 and false)

if 1 or 0:
        print(True or 0 or False)
if not 1:
        print(not 1)        