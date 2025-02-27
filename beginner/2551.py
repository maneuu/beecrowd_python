while True:
    try:
        n_treinos = int(input().strip())  # Lê o número de treinos
        recorde_atual = 0  # Guarda a maior média encontrada

        for i in range(n_treinos):
            tempo, distancia = map(int, input().split())
            media = distancia / tempo

            if media > recorde_atual:  # Se a nova média for maior que o recorde atual
                print(i + 1)
                recorde_atual = media  # Atualiza o recorde

    except EOFError:
        break  # Para quando chegar no fim do arquivo (EOF)
