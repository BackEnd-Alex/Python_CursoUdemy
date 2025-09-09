#Execultando laço de repetição while
contador = 0

while contador < 100:
    contador += 1
  
    if contador == 6:
       print('Não vou mostar o 6')
       continue
    if contador >= 10 and contador <= 15:
        print('Não vou mostrar o', contador)
        continue
    print(contador)
    if contador == 40:
        break

print('Acabou!')