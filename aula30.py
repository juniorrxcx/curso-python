'''

Sempre pensar em como
eu posso diminuir o codigo
de forma que ele fique mais legivel

'''
velocidade = 61
local_carro = 101

#Em letra maiuscula a variavel nao muda de valor
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE)\
      and local_carro <= (LOCAL_1 + RADAR_RANGE)\
        and vel_carro_passou_radar_1

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print("Velocidade carro passou do radar 1")

if carro_multado_radar_1:
    print("Carro multado em radar 1")