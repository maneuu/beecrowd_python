def main():
    casos = int(input())  # Número de casos de teste
    for _ in range(casos):
        ano_evento = int(input())  # Ano fornecido na entrada
        if ano_evento >= 2015:
            print(f"{ano_evento - 2015 + 1} A.C.")  # Evento aconteceu Antes de Cristo
        else:
            print(f"{2015 - ano_evento} D.C.")  # Evento aconteceu Depois de Cristo

main()