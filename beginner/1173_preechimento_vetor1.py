def main():
    # Lê o primeiro valor
    valor = int(input())
    
    # Inicializa o vetor com o primeiro valor
    vetor = [valor]
    
    # Imprime o primeiro valor
    print(f"N[0] = {vetor[0]}")
    
    # Preenche o vetor com os próximos valores, multiplicando o valor anterior por 2
    for i in range(1, 10):
        valor *= 2  # Multiplica o valor por 2
        vetor.append(valor)  # Adiciona o novo valor ao vetor
        print(f"N[{i}] = {vetor[i]}")  # Imprime o valor no formato desejado

main()
