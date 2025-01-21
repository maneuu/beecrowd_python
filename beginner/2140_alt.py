while True:
    notas = [2, 5, 10, 20, 50, 100]
    c, d = map(int, input().split())
    if (c, d) == (0, 0):
        break

    troco = d - c
    possivel = False
    for n in notas:
        if troco - n in notas:
            possivel = True
            break
    print("possible" if possivel else "impossible")
