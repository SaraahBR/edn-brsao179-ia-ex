'''
3. Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres 
e conter pelo menos um número. 
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
'''

def verificar_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()

        if senha.lower() == 'sair':
            print("Encerrado pelo usuário.")
            break

        if len(senha) < 8:
            print("Senha fraca: deve conter pelo menos 8 caracteres.")
            continue

        if not any(char.isdigit() for char in senha):
            print("Senha fraca: deve conter pelo menos um número.")
            continue

        print("Senha forte! A senha atende aos critérios de segurança.")
        break

verificar_senha()