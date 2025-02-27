def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        qtd_moedas = int(input())
        moedas = [int(input()) for _ in range(qtd_moedas)]
        saltos = int(input())

        # Inverte a lista para começar do topo do cilindro
        moedas = moedas[::-1]

        # Soma os elementos a cada N saltos na lista invertida
        soma_moedas = sum(moedas[i] for i in range(0, qtd_moedas, saltos))

        if eh_primo(soma_moedas):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")

    except EOFError:
        break