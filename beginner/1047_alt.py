def main():
    # Lê as horas e minutos de início e fim do jogo
    hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())
    
    # Caso especial: o jogo começa e termina exatamente no mesmo horário e minuto
    if hora_inicial == hora_final and minuto_inicial == minuto_final:
        diferenca_horas = 24  # Duração máxima de 24 horas
        diferenca_minutos = 0
    else:
        # Converte horas para minutos e soma os minutos (para facilitar o cálculo)
        inicio_total = hora_inicial * 60 + minuto_inicial
        final_total = hora_final * 60 + minuto_final
        
        # Calcula a diferença total em minutos, considerando o ciclo de 24 horas (1440 minutos)
        if final_total < inicio_total:
            diferenca_total = (final_total + 1440) - inicio_total
        else:
            diferenca_total = final_total - inicio_total
        
        # Converte a diferença total de minutos para horas e minutos
        diferenca_horas = diferenca_total // 60
        diferenca_minutos = diferenca_total % 60
    
    # Exibe o resultado formatado
    print(f"O JOGO DUROU {diferenca_horas} HORA(S) E {diferenca_minutos} MINUTO(S)")

main()
