while True:
    try:
        mes, dia = map(int, input().split())
        
        if mes == 12:
            if dia == 25:
                print("E natal!")
            elif dia == 24:
                print("E vespera de natal!")
            elif dia < 25:
                print(f"Faltam {25 - dia} dias para o natal!")
            else:
                print("Ja passou!")
        else:
            dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            dias_restantes = (dias_por_mes[mes - 1] - dia)  # Dias restantes no mês atual
            dias_restantes += sum(dias_por_mes[mes:11])  # Dias dos meses até novembro
            dias_restantes += 25   # Dias de dezembro até o Natal
            print(f"Faltam {dias_restantes} dias para o natal!")
    except EOFError:
        break
