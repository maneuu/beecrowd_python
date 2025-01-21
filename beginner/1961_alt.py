def verificar_jogo(pulos_maximos, alturas_dos_canos):
    for i in range(len(alturas_dos_canos) - 1):
        if abs(alturas_dos_canos[i] - alturas_dos_canos[i + 1]) > pulos_maximos:
            return "GAME OVER"
    return "YOU WIN"

def main():
    pulos_maximos, total_canos = map(int, input().split())  # Recebe as informações de pulo máximo e número de canos
    alturas_dos_canos = list(map(int, input().split()))  # Recebe as alturas dos canos

    resultado = verificar_jogo(pulos_maximos, alturas_dos_canos)
    print(resultado)

main()
