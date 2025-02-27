def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        moedas = []
        qtd_moedas = int(input())
        for _ in range(qtd_moedas):
            moeda = int(input())
            moedas.append(moeda)

        moedas.reverse()
        soma_moedas = 0
        saltos = int(input())
        for i in range(0,qtd_moedas,saltos):
            soma_moedas += moedas[i]
            
        if eh_primo(soma_moedas):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
            
    except EOFError:break

