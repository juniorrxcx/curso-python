qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    print(linha)

    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1

    linha +=1

print('Acabou')

'''

Para cada linha que ele roda, ele roda 
outro while com 5 colunas dentro dela

'''