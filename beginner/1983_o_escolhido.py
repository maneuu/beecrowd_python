def main():
    num_casos = int(input())
    alunos = {}

    for _ in range(num_casos):
        matricula, nota = [float(num) for num in input().split()]
        alunos[matricula] = nota

    maior_nota = max(alunos.values())
    if maior_nota < 8:
        print("Mininum note not reached")
    else:
        for matricula, nota in alunos.items():
            if nota == maior_nota:
                print(f"{matricula:.0f}")
                break

main()
