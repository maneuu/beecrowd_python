caso = 0
while True:
    try:
        caso += 1
        sub = input()
        seq = input()

        if sub in seq:
            qtd = seq.count(sub) 
            ultima_pos = seq.rfind(sub) + 1
            
            print(f"Caso #{caso}:")
            print(f"Qtd.Subsequencias: {qtd}")
            print(f"Pos: {ultima_pos}",end="\n\n")

        else:
            print(f"Caso #{caso}:")
            print("Nao existe subsequencia",end="\n\n")
    except EOFError:
        break
