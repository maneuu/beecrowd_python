while True:
    try:
        qtd_pessoas, qtd_datas = [int(valor) for valor in input().split()]
        datas_disponiveis = []

        for _ in range(qtd_datas):
            entrada = [valor for valor in input().split()]
            datas_disponiveis.append(entrada)

        encontrado = False
        data_escolhida = None

        for i in range(qtd_datas):
            total_presentes = 0
            for j in range(1, qtd_pessoas + 1):
                total_presentes += int(datas_disponiveis[i][j])
            if encontrado:
                break
            if total_presentes == qtd_pessoas:
                data_escolhida = datas_disponiveis[i][0]
                encontrado = True

        print(data_escolhida if encontrado else "Pizza antes de FdI")
    except EOFError: break