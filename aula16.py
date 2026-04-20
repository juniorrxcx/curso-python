entrada = input('Voce quer "entrar", "sair" ou "pausar"? ')

if entrada == 'entrar':
    print('Voce entrou no sistema')
    print('op1')
elif entrada == 'sair':
    print('Voce saiu do sistema')
    print('op2')
elif entrada == 'pausar':
    print('Voce pausou o sistema')
    print('op3')
else:
    print('Voce nao digitou "entrar" nem "sair"')
    print('else')