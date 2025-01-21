def main():
    caso = 0
    while True:
        try: 
            caso += 1
            valor = int(input())
            numeros = ["0"]

            for n in range(1 , valor+1):
                for _ in range(n):
                    numeros.append(str(n))


            print(f"Caso {caso}: {len(numeros)} {'numeros' if len(numeros) > 1 else 'numero'}")
            print(" ".join(numeros),end="\n\n")
        except EOFError:
            break
main()