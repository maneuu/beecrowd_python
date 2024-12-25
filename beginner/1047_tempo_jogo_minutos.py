"""Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

"""
# esse codigo há um erro e optei desistir e obter a resposta ;-;
# meu codigo final porem esta com o erro
def main():
    hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())
    
    if hora_inicial == hora_final and minuto_inicial == minuto_final:
        diferenca_horas = 24
        diferenca_minutos = 0

    else:
        hora_inicial *= 60
        hora_final *= 60
        
        diferenca = (hora_final + minuto_final) - (hora_inicial + minuto_inicial)
        diferenca_horas = diferenca//60
        diferenca_minutos = diferenca - (diferenca_horas * 60)
    
    print(f"O JOGO DUROU {diferenca_horas} HORA(S) E {diferenca_minutos} MINUTO(S)")
    

main()
'''
O erro acontece sempre que a hora final é menor que a hora inicial (jogos que ultrapassam a meia-noite). Nesse caso, o cálculo direto 
(hora_final+minuto_final) − (hora_inicial+minuto_inicial)
gera um valor negativo, porque o código não considera o ciclo de 24 horas  (1440 minutos).
'''