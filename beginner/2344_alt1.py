N = int(input())

intervalos = [
    (0, 0, 'E'),
    (1, 35, 'D'),
    (36, 60, 'C'),
    (61, 85, 'B'),
    (86, 100, 'A')
]

for inicio, fim, saida in intervalos:
    if inicio <= N <= fim:
        print(saida)
        break