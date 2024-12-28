def main():
    nota_validas = soma = 0
    
    while nota_validas < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            nota_validas += 1
            soma += nota
    media = soma/2
    print(f"media = {media:.2f}")

main()