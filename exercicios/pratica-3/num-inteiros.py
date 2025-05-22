'''
4. Crie um programa que solicite ao usuário que insira números inteiros. 
O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, 
o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, 
o programa deve informar o erro e continuar. No final, o programa deve exibir a quantidade de números 
pares e ímpares inseridos.
'''

def contar_pares_impares():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip()

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1
        except ValueError:
            print("Erro: entrada inválida. Digite apenas números inteiros ou 'fim' para encerrar.")

    print("\n--- Resultado Final ---")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


contar_pares_impares()