a1, a2, a3 = (int(input()) for _ in range(3))

tempo_primeiro = a2 * 2 + a3 * 4
tempo_segundo = a1 * 2 + a3 * 2
tempo_terceiro = a1 * 4 + a2 * 2

print(min(tempo_primeiro, tempo_segundo, tempo_terceiro))
