# Loop principal para capturar a entrada até o final do arquivo
while True:
    try:
        # Captura o número de casos
        num_casos = int(input())
        
        # Lista para armazenar os números das expressões
        expressoes_numericas = []
        
        # Captura as expressões numéricas e armazena em uma lista
        for _ in range(num_casos):
            entrada = input()
            # Substitui o sinal de '=' por espaço e divide os números
            numeros = list(map(int, entrada.replace('=', ' ').split()))
            expressoes_numericas.append(numeros)
        
        # Lista para armazenar as suposições dos usuários
        # (NOME) (EXPRESSÃO ESCOLHIDA) RESULTADO(+ - * I)
        suposicoes = []
        
        # Captura as suposições dos usuários
        for _ in range(num_casos):
            resposta = input().split()
            suposicoes.append(resposta)

        # Lista para armazenar os usuários que falharam
        usuarios_falharam = []

        # Verifica cada caso
        for i in range(num_casos):
            # Pega o índice da expressão a ser verificada
            indice = int(suposicoes[i][1]) - 1
            num1 = expressoes_numericas[indice][0]
            num2 = expressoes_numericas[indice][1]
            resultado_esperado = expressoes_numericas[indice][-1]

            # Se a resposta for 'I' (Incorreto), verifica operações básicas
            if suposicoes[i][2] == "I":
                if int(num1) + int(num2) == int(resultado_esperado) or \
                   int(num1) - int(num2) == int(resultado_esperado) or \
                   int(num1) * int(num2) == int(resultado_esperado):
                    usuarios_falharam.append(suposicoes[i][0])
            else:  # Se a resposta for 'C' (Correto), verifica a operação indicada
                expressao = f"{num1} {suposicoes[i][2]} {num2}"
                resultado_calculado = eval(expressao)
                if resultado_calculado != int(resultado_esperado):
                    usuarios_falharam.append(suposicoes[i][0])
        
        # Exibe o resultado com base no número de falhas
        if len(usuarios_falharam) == 0:
            print("You Shall All Pass!")
        elif len(usuarios_falharam) == num_casos:
            print("None Shall Pass!")
        else:
            # Ordena os usuários que falharam em ordem alfabética
            usuarios_falharam.sort()
            for i in range(len(usuarios_falharam) - 1):
                print(usuarios_falharam[i], end=" ")
            print(usuarios_falharam[-1])  # Imprime o último nome com quebra de linha

    except EOFError:  # Se o fim do arquivo for alcançado, encerra o loop
        break
