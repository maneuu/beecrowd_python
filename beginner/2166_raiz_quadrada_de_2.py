n = int(input())
fracao = 0
for _ in range(n):
    fracao = 1 / (2 + fracao)

resultado = 1 + fracao
print(f"{resultado:.10f}")