def main():
    hora_saida, duracao_viagem, hora_atual = [int(num) for num in input().split()]
    resultado = hora_saida + duracao_viagem + hora_atual
    if resultado >= 24:
        resultado -= 24
    elif resultado < 0:
        resultado = 24 + resultado
    print(resultado)
main()
