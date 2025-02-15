while True:
    try:
        # Número de casos
        n = int(input())
        
        expressoes = [list(map(int, input().replace('=', ' ').split())) for _ in range(n)]
        suposicoes = [input().split() for _ in range(n)]
        
        falharam = []
        
        for i in range(n):
            nome, indice, operacao = suposicoes[i]
            indice = int(indice) - 1
            num1, num2, resultado = expressoes[indice]

            # Verifica se a operação está correta ou incorreta
            if operacao == 'I':
                if num1 + num2 == resultado or num1 - num2 == resultado or num1 * num2 == resultado:
                    falharam.append(nome)
            else:
                expressao = f"{num1} {operacao} {num2}"
                if eval(expressao) != resultado:
                    falharam.append(nome)
        
        # Resultado baseado nas falhas
        if not falharam:
            print("You Shall All Pass!")
        elif len(falharam) == n:
            print("None Shall Pass!")
        else:
            falharam.sort()
            print(" ".join(falharam))
    
    except EOFError:
        break
