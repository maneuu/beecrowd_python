input()
numeros = [int(num) for num in input().split()]

def mult(multiplo):
    resultado = sum(1 for num in numeros if num % multiplo == 0)
    return resultado


for n in range(2,6):
    print(f"{mult(n)} Multiplo(s) de {n}")