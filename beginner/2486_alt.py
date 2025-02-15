tabela_vitamina_c = {
    "suco de laranja": 120,
    "morango fresco": 85,
    "mamao": 85,
    "goiaba vermelha": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34
}

while True:
    # Ler número de casos
    num_alimentos = int(input())
    
    # Condição de parada
    if num_alimentos == 0:
        break
    
    # Processar cada alimento
    consumo = []
    for _ in range(num_alimentos):
        entrada = input().strip().split(maxsplit=1)
        quantidade = int(entrada[0])
        alimento = entrada[1]
        consumo.append((quantidade, alimento))
    
    # Calcular total de vitamina C
    total_vitamina_c = 0
    for qtd, item in consumo:
        total_vitamina_c += qtd * tabela_vitamina_c[item]
    
    # Verificar necessidade de ajuste
    if total_vitamina_c > 130:
        deficit = total_vitamina_c - 130
        print(f"Menos {deficit} mg")
    elif total_vitamina_c < 110:
        adicional = 110 - total_vitamina_c
        print(f"Mais {adicional} mg")
    else:
        print(f"{total_vitamina_c} mg")