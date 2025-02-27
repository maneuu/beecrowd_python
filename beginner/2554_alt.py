while True:
    try:
        qtd_pessoas, qtd_datas = map(int, input().split())
        data_escolhida = "Pizza antes de FdI"

        datas_disponiveis = [input().split() for _ in range(qtd_datas)]

        for entrada in datas_disponiveis:
            data, presencas = entrada[0], map(int, entrada[1:])
            if sum(presencas) == qtd_pessoas:
                data_escolhida = data
                break

        print(data_escolhida)
    except EOFError:
        break
