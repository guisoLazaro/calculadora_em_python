while(True):
    print("=====================")
    print("     Calculadora     ")
    print("=====================")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    print("=====================")
    try:
        op = input()
        if(op == '1'):
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            result = num1 + num2
            print(f"Resultado da Soma: {result}")
        elif(op == '2'):
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            result = num1 - num2
            print(f"Resultado da Subtração: {result}")
        elif(op == '3'):
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            result = num1 * num2
            print(f"Resultado da Multiplicação: {result}")
        elif(op == '4'):
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            result = num1 / num2
            print(f"Resultado da Divisão: {result}")
        elif(op == '5'):
            break
        else:
            print("Opção inválida, tente novamente")
    except Exception as error:
        print(error)

        