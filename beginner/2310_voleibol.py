num_jogadores = int(input())
T = {
    'S': 0,
    'B': 0,
    'A': 0,
}
SU = {
    'S': 0,
    'B': 0,
    'A': 0,
}
for _ in range(num_jogadores):
    # NOME DO JOGADOR
    input()
    # VALORES TOTAIS
    S,B,A = [int(x) for x in input().split()]
    T['S'] += S
    T['B'] += B
    T['A'] += A
    # VALORES COM SUCESSO
    S1,B1,A1 = [int(x) for x in input().split()]
    SU['S'] += S1
    SU['B'] += B1
    SU['A'] += A1

print(f"Pontos de Saque: {SU['S']*100/T['S']:.2f} %.")
print(f"Pontos de Bloqueio: {SU['B']*100/T['B']:.2f} %.")
print(f"Pontos de Ataque: {SU['A']*100/T['A']:.2f} %.")