T = int(input())
for _ in range(T):
    nome = input()
    GD = float(input())
    valores = [float(n) for n in input().split()]
    valores.remove(max(valores))
    valores.remove(min(valores))
    resultado = sum(valores) * GD
    print(f"{nome} {resultado:.2f}")