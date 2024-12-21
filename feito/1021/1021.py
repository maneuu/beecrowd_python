reais, centavos = map(int, input().split('.'))
# split() separa os valores por ponto, e map(int, ...) converte os valores para inteiros
# Exemplo: 576.73 -> reais = 576, centavos = 73
# Exemplo: 4.00 -> reais = 4, centavos = 0
# Não se pode usar float(input()) pois split() não aceita float apenas string

# Converte o valor total em centavos
centavos = centavos + reais * 100

# Lista de notas disponíveis
notas = [100, 50, 20, 10, 5, 2]

print('NOTAS:')
# Calcula a quantidade de cada nota necessária
for nota in notas:
    qtd = centavos // (nota * 100)
    print(f'{qtd} nota(s) de R$ {nota}.00')
    centavos = centavos % (nota * 100)

# Lista de moedas disponíveis
moedas = [100, 50, 25, 10, 5, 1]

print('MOEDAS:')
# Calcula a quantidade de cada moeda necessária
for moeda in moedas:
    qtd = centavos // moeda
    print(f'{qtd} moeda(s) de R$ {moeda // 100}.{moeda % 100:02}')
    centavos = centavos % moeda
