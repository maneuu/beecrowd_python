formulario = input()
tamanho = len(formulario)

# Dicionário para mapear as condições
resposta = {True: "YES", False: "NO"}

# Imprime o resultado com base na condição
print(resposta[tamanho <= 80])
