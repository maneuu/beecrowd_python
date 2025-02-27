# O dicionário 'operacoes' mapeia as opções ('max', 'min', 'mean', 'eye') para funções lambda.
# As funções lambda são usadas aqui para definir operações simples de forma compacta.
# Cada função recebe 'valores' (uma lista de valores RGB) como argumento e realiza a operação correspondente.
operacoes = {
    "max": lambda valores: max(valores),  # Retorna o maior valor da lista.
    "min": lambda valores: min(valores),  # Retorna o menor valor da lista.
    "mean": lambda valores: int(sum(valores) / 3),  # Calcula a média aritmética e converte para inteiro.
    "eye": lambda valores: int(valores[0] * 0.3 + valores[1] * 0.59 + valores[2] * 0.11)  # Cálculo ponderado para 'eye'.
}

for i in range(int(input())):
    conversao = input()  # min / max / mean / eye
    valores_rgb = [int(X) for X in input().split()]

    print(f"Caso #{i+1}: {operacoes[conversao](valores_rgb)}")
