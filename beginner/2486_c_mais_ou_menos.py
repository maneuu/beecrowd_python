tabela = {
    "suco de laranja" : 120,
    "morango fresco" : 85,
    "mamao" : 85,
    "goiaba vermelha" : 70,
    "manga" : 56,
    "laranja" : 50,
    "brocolis" : 34
}
# 110 130
while True:
    casos = int(input())
    if casos == 0: break
    valores = []
    for _ in range(casos):
        qtd, alimento = input().split(maxsplit=1)
        qtd = int(qtd)
        valores.append(qtd)
        valores.append(alimento)
    total = 0
    for i in range(0,len(valores),2):
        total += valores[i] * tabela[valores[i+1]]

    if total > 130:
        print(f"Menos {total - 130} mg")
    elif total < 110:
        print(f"Mais {110 - total} mg")
    else:
        print(f"{total} mg")