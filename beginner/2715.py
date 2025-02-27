while True:
    try:
        n = int(input().strip())
        valores = list(map(int, input().split()))

        total = sum(valores)
        soma_rangel = 0
        menor_diferenca = total  

        for i in range(n - 1):
            soma_rangel += valores[i]
            soma_gugu = total - soma_rangel
            diferenca = abs(soma_rangel - soma_gugu)
            if diferenca < menor_diferenca:
                menor_diferenca = diferenca

        print(menor_diferenca)

    except EOFError:
        break
