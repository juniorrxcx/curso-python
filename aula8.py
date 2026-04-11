from datetime import date

nome = "Junior"
sobrenome = "Lima"
idade = 21
ano_nascimento = (date.today().year) - idade
maior_de_idade = idade >= 18
altura_metros = 1.73

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)