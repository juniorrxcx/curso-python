# IMC = peso / (altura * altura)
nome = "Junior Lima"
altura = 1.73
peso = 60
imc = peso / (altura ** 2)

linha1 = f'{nome}, tem {altura:.1f} de altura pesa {peso} quilos e seu IMC é {imc:.2f}' 

print(nome, "tem ", altura, "de altura\n"\
      "pesa", peso, "quilos e seu IMC é", imc )

print("-" * 10)

print(linha1)