abas, n = [int(num) for num in input().split()]
acoes = []
for _ in range(n):
    acoes.append(input())
fechadas = acoes.count("fechou")
clicadas = acoes.count("clicou")
resultado = abas - clicadas + fechadas
print(resultado)
