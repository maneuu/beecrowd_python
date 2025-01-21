def converter_para_dias(mes, dia):
    dias_por_mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    dias_acumulados = sum(dias_por_mes[:mes])
    return 366 - 6 - (dias_acumulados + dia)

while True:
    try:
        mes, dia = [int(num) for num in input().split()]
        if mes == 12:
            if dia == 25:
                print("E natal!")
            elif dia == 24:
                print("E vespera de natal!")
            elif dia < 24:
                print(f"Faltam {25 - dia} para o natal!")
            else:
                print("Ja passou!")
        else:

            print(f"Faltam {converter_para_dias(mes,dia)} dias para o natal!") 
    except EOFError:
        break