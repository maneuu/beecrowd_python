def main():
    while True:
        senha = int(input())
        print("Acesso Permitido" if senha == 2002 else "Senha Invalida")
        if senha == 2002:
            break

main()
