'''
1. Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão)
entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. 
Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.​
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).​
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.​
Trate os seguintes erros:​
Entrada inválida (não numérica) para os números​
Divisão por zero​
Operação inválida​
Use try/except para capturar e tratar os erros apropriadamente.​
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.​
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

'''

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número válido.")

    while True:
        try:
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número válido.")

    while True:
        operador = input("Digite a operação (+, -, *, /): ")
        
        if operador == '+':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
            break

        elif operador == '-':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
            break

        elif operador == '*':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
            break

        elif operador == '/':
            try:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
                break
            except ZeroDivisionError:
                print("Erro: divisão por zero não é permitida.")
                while True:
                    try:
                        num2 = float(input("Digite um novo segundo número (diferente de zero): "))
                        if num2 != 0:
                            break
                        else:
                            print("O número ainda é zero. Tente novamente.")
                    except ValueError:
                        print("Erro: entrada inválida. Por favor, digite um número válido.")
        else:
            print("Erro: operação inválida. Use apenas +, -, * ou /.")

calculadora()