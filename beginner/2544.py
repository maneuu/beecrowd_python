while True:
    try:
        valor = int(input())
        from math import log2
        resultado = int(log2(valor))
        print(resultado)
    except EOFError: break