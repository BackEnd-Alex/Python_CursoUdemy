#Senha valida

"""print("Entrada")
senha  = int(input())
while senha != 2002:
    print("Senha Invalida")
    senha  = int(input())
print("Acesso Permitido")   """

print("Entrada")
alcool = 0
gasolina = 0
diesel = 0

combustivel = int(input())
#cont = 0
while combustivel != 4:

    if combustivel == 1:
        alcool += 1     
    elif combustivel == 2:
        gasolina += 1
    elif combustivel == 3:
        diesel += 1
        
    combustivel = int(input())
print("MUITO OBRIGADO")
print("Alcool: {}".format(alcool))
print("Gasolina: {}".format(gasolina))
print("Diesel: {}".format(diesel))
