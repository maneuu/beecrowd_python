def main():

    regras = {
    'ataque': {'pedra': True, 'papel': True, 'ataque': "Aniquilacao mutua"},
    'pedra': {'pedra': 'Sem ganhador', 'papel': True, 'ataque': False},
    'papel': {'papel': 'Ambos venceram', 'pedra': False, 'ataque': False}
    }
    casos = int(input())
    for _ in range(casos):
        jogador_1 = input()
        jogador_2 = input()
        
        resultado = regras[jogador_1][jogador_2]

        if type(resultado) == str:
            print(resultado)
        else:
            if resultado:
                print("Jogador 1 venceu")
            else:
                print("Jogador 2 venceu")
main()