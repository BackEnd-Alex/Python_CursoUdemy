nome = 'Alex'
preco = 1000.95897643
variavel = '%s, o preço é de R$ %.2f' % (nome, preco)
print(variavel)
print ('O hexadecimal de %d é %08x' % (1500, 1500))

print('--------------------------------')
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.95897643:0>10.2f}')
print(f'{1000.95897643:0<10.2f}')
print(f'{1000.95897643:^10.2f}')
print(f'{nome.lower():^10}')
print(f'{nome.upper():^10}')
print(f'{nome.title():^10}')

