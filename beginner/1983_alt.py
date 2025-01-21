def main():
    num_casos = int(input())
    matriculas = []
    notas = []

    for _ in range(num_casos):
        matricula, nota = input().split()
        matriculas.append(matricula)
        notas.append(float(nota))

    maior_nota = max(notas)
    
    if maior_nota < 8:
        print("Minimum note not reached")
    else:
        # Encontramos o índice da maior nota e usamos esse índice para pegar a matrícula correspondente
        indice_maior_nota = notas.index(maior_nota)
        print(matriculas[indice_maior_nota])

main()
