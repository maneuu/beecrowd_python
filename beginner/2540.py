while True:
    try: 
        jogadores = int(input())
        votos = [int(X) for X in input().split()]
        afavor = 0
        for voto in votos:
            if voto == 1:
                afavor += 1
        
        if (afavor/jogadores) >= (2/3):
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break
    