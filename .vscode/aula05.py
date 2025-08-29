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