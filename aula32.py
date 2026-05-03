"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n1 = input("Digite um número inteiro: ")

if n1.isdigit():
    entrada_int = int(n1)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print("voce não digitou um numero inteiro")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input("Digite a hora em num inteiro: "))

if (hora >=0 ) and (hora <= 11):
    print("Bom dia")

if (hora >=12 ) and (hora <= 17):
    print("Boa tarde")

if (hora >=18 ) and (hora <= 23):
    print("Boa noite")




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é curto")

if (tamanho_nome >= 5) and (tamanho_nome <= 6):
    print("Seu nome é normal")

if tamanho_nome > 6:
    print("Seu nome é muito grande")