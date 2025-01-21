def main():
    input()  # Lê o número de estrelas (não usado diretamente)
    carneiros = [int(num) for num in input().split()]  # Lê o número de carneiros em cada estrela
    carneiros_originais = carneiros.copy()  # Cópia dos carneiros para comparar depois
    posicao = 0  # Posição inicial do irmão
    carneiros_roubados = 0  # Contador de carneiros roubados

    while 0 <= posicao < len(carneiros):  # Enquanto estiver dentro dos limites
        posicao_atual = carneiros[posicao]
        if carneiros[posicao] > 0:  # Se a estrela tem carneiros
            carneiros_roubados += 1  # Rouba um carneiro
            carneiros[posicao] -= 1  # Diminui o número de carneiros na estrela

        if posicao_atual % 2 == 0:  # Se o número de carneiros é par
            posicao -= 1  # Vai para a estrela anterior
        else:  # Se for ímpar
            posicao += 1  # Vai para a próxima estrela

    # Número de estrelas atacadas: onde os carneiros mudaram
    estrelas_atacadas = sum(1 for i in range(len(carneiros)) if carneiros[i] < carneiros_originais[i])

    # Carneiros não roubados
    carneiros_nao_roubados = sum(carneiros)

    # Imprime a quantidade de estrelas atacadas e carneiros não roubados
    print(f"{estrelas_atacadas} {carneiros_nao_roubados}")

main()
