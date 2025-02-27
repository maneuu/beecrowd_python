valores = [int(input()) for _ in range(3)]

primeiro_andar = valores[1] * 2 + valores[2] * 4
segundo_andar = valores[0] * 2 + valores[2] * 2
terceiro_andar = valores[0] * 4 + valores[1] * 2

print(min(primeiro_andar, segundo_andar, terceiro_andar))