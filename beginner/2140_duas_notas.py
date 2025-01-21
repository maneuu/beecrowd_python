while True:
    notas = [2, 5, 10, 20, 50, 100]
    c, d = map(int, input().split())
    if (c, d) == (0, 0):
        break

    troco = d - c
    possivel = False
    for n1 in notas:
        for n2 in notas:
            if n1 + n2 == troco:
                possivel = True
                break
        if possivel: break
    print("possible" if possivel else "impossible")
