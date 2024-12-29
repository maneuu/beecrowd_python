def main():
    usuarios = somatorio = 0
    while True:
        idade = int(input())
        if idade < 0:
            break
        somatorio += idade
        usuarios += 1
    
    media = somatorio/usuarios
    print(f"{media:.2f}")
main()