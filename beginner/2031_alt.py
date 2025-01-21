def main():
    regras = {
        'ataque': {'pedra': "Jogador 1 venceu", 'papel': "Jogador 1 venceu", 'ataque': "Aniquilacao mutua"},
        'pedra': {'pedra': 'Sem ganhador', 'papel': "Jogador 1 venceu", 'ataque': "Jogador 2 venceu"},
        'papel': {'papel': 'Ambos venceram', 'pedra': "Jogador 2 venceu", 'ataque': "Jogador 2 venceu"}
    }
    
    casos = int(input())
    
    for _ in range(casos):
        jogador_1 = input().strip()
        jogador_2 = input().strip()
        
        resultado = regras[jogador_1][jogador_2]
        print(resultado)

main()
