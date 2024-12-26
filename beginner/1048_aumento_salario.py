"""Salário	                  Percentual de Reajuste
0 - 400.00 ================== 15%
400.01 - 800.00 ============= 12%
800.01 - 1200.00 ============ 10%
1200.01 - 2000.00 ============ 7%
Acima de 2000.00 =  ========== -4%

"""
# codigo final/ poderia ter simplificado mais :/

def main():
    salario = float(input())
    if 0 <= salario <= 400:
        novo_salario = (salario * 115) / 100
        aumento = novo_salario - salario
        percentual = 15

    elif 400 < salario <= 800:
        novo_salario = (salario * 112) / 100
        aumento = novo_salario - salario
        percentual = 12

    elif 800 < salario <= 1200:
        novo_salario = (salario * 110) / 100
        aumento = novo_salario - salario
        percentual = 10

    elif 1200 < salario <= 2000:
        novo_salario = (salario * 107) / 100
        aumento = novo_salario - salario
        percentual = 7

    elif salario > 2000:
        novo_salario = (salario * 104) / 100
        aumento = novo_salario - salario
        percentual = 4
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {percentual:.0f} %")

main()