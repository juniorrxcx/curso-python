#Calculadora com while

while True:
    print('=' * 20)
    n1 = input("Digite o primeiro número: ")
    n2 = input("Digite o segundo número: ")
    operador = input("Digite o operador (+-/*): ")

    numeros_validos = None
    print('=' * 20)

    # Checa se os numeros são validos
    try: 
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True

    except:
        numeros_validos = None
        print('Error')
    
    if numeros_validos is None:
        print("Um ou ambos os números digitados são invalidos")
        continue

    # Checa se o operador é permitido
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print("Operador invalido")
        continue
    
    # Checa se foi digitado somente um operador
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print("Realizando a sua conta. Confira o resultado abaixo:")
    if operador == '+':
        print(n1_float + n2_float)
    elif operador == '-':
        print(n1_float - n2_float)
    elif operador == '/':
        print(n1_float / n2_float)
    elif operador == '*':
        print(n1_float * n2_float)
    else:
        print("Nunca deveria chegar até aqui")

    print('=' * 20)


    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break