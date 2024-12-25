def main():
    hora_inicial, hora_final = map(int, input().split())
    diferenca = 24 if hora_inicial == hora_final else (hora_final - hora_inicial + 24) % 24
    print(f"O JOGO DUROU {diferenca} HORA(S)")

main()
