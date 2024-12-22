N = float(input())


print("NOTAS:")
notas = N / 100
print(f"{int(notas)} nota(s) de R$ 100.00")
N = N % 100

notas = N / 50
print(f"{int(notas)} nota(s) de R$ 50.00")
N = N % 50

notas = N / 20
print(f"{int(notas)} nota(s) de R$ 20.00")
N = N % 20

notas = N / 10
print(f"{int(notas)} nota(s) de R$ 10.00")
N = N % 10

notas = N / 5
print(f"{int(notas)} nota(s) de R$ 5.00")
N = N % 5

notas = N / 2
print(f"{int(notas)} nota(s) de R$ 2.00")
N = N % 2

print("MOEDAS:")
moedas = N / 1.00
print(f"{int(moedas)} moeda(s) de R$ 1.00")
N = N % 1.00

moedas = N / 0.50
print(f"{int(moedas)} moeda(s) de R$ 0.50")
N = N % 0.50

moedas = N / 0.25
print(f"{int(moedas)} moeda(s) de R$ 0.25")
N = N % 0.25

moedas = N / 0.10
print(f"{int(moedas)} moeda(s) de R$ 0.10")
N = N % 0.1

moedas = N / 0.05
print(f"{int(moedas)} moeda(s) de R$ 0.05")
N = N % 0.05

moedas = float(N / 0.01)
print(f"{int(moedas)} moeda(s) de R$ 0.01")