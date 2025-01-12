def main():
    num_pessoas = int(input())  # Número de pessoas
    golpes_por_pessoa = list(map(int, input().split()))  # Lista com os golpes para cada pessoa
    pessoa_com_menor_golpe = golpes_por_pessoa.index(min(golpes_por_pessoa)) + 1  # Índice da pessoa com menos golpes (ajustado para começar em 1)
    print(pessoa_com_menor_golpe)

main()
