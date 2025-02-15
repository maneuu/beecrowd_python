while True:
    try:
        gameplays, my_id = [int(X) for X in input().split()]
        jogos = 0
        for i in range(gameplays):
            identificador, jogo = [int(X) for X in input().split()]
            if (identificador == my_id) and (jogo == 0):
                jogos += 1
        print(jogos)
    except EOFError: break