def main():
    soma = nota_valida = 0
    while True:
        nota = float(input())
        if nota > 10 or nota < 0:
            print("nota invalida")
        else: 
            soma += nota
            nota_valida += 1
            
        if nota_valida == 2:
            print(f"media = {soma/2:.2f}")

            while True:
                repetir = int(input("novo calculo (1-sim 2-nao)\n"))
                if repetir in [1,2]:
                    break
            soma = nota_valida = 0

            if repetir == 2:
                break 
        
main()