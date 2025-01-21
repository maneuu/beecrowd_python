while True:
    n = int(input())  # Número total de entradas (casos de teste)
    if not n:  # Se n for 0, encerra o programa
        break
    pedidos = []  # Lista para armazenar o número de pedidos por pessoa
    while n:  # Processa todas as pessoas
        n -= 1  # Diminui o contador de casos restantes
        x = int(input())  # Número de pessoas na mesa
        if x % 2 == 0:  # Se o número for par
            pedidos.append((2 * x) - 2)  # Calcula pedidos para par
        else:  # Se o número for ímpar
            pedidos.append((2 * x) - 1)  # Calcula pedidos para ímpar
    for p in pedidos:  # Itera pela lista de pedidos
        print(p)  # Imprime cada soma calculada
# questão mal estruturada, tive que pesquisar a resposta porem ja tinha noção de como realizar