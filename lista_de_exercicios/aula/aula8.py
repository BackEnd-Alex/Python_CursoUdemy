"""
CONSTANTE = Variáveis, que não vão mudar de valor durante a execução do programa.
Muitas condiçoes no mesmo if(ruim)
<- contagem de complexidade.
"""
velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local onde o carro está
RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # Alcance do radar 1

velocidade_passou_radar1 = velocidade > RADAR_1
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    velocidade > RADAR_1

if velocidade_passou_radar1:
    print('Velocidade carro passou do radar 1')


if carro_multado and velocidade_passou_radar1:
      print('Carro foi multado no radar 1')
