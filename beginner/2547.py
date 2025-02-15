while True:
    try:
        visitantes, a_min, a_max = [int(X) for X in input().split()]
        resultado = 0
        for _ in range(visitantes):
            altura = int(input())
            if (altura >= a_min) and (altura <= a_max):
                resultado += 1
        print(resultado)
    except EOFError:break