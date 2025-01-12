def main():
    while True:
        informacoes = [int(num) for num in input().split()]

        if informacoes[0] == 0: break

        area_casa = int(informacoes[0] * informacoes[1])
        percentual_permitido = informacoes[2]
        area_terreno = (area_casa * 100)/percentual_permitido
        lado_terreno = int(area_terreno**0.5)
        print(lado_terreno)

main()