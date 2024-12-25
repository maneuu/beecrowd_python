'''Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
16 2

O JOGO DUROU 10 HORA(S)

0 0

O JOGO DUROU 24 HORA(S)

2 16

O JOGO DUROU 14 HORA(S)'''

def main():
    hora_inicial, hora_final = map(int, input().split())
    
    # Calcula a diferença de horas no ciclo de 24 horas:
    # 1. (hora_final - hora_inicial): diferença direta entre as horas.
    # 2. + 24: garante que o resultado seja positivo mesmo se hora_final < hora_inicial.
    # 3. % 24: ajusta o resultado para o intervalo de 0 a 23 horas (ciclo de um dia).
    diferenca = (hora_final - hora_inicial + 24) % 24
    
    # Caso especial: se a diferença for 0 (ou seja, hora_inicial == hora_final),
    # significa que o jogo durou exatamente 24 horas.
    if diferenca == 0:
        diferenca = 24
    
    print(f"O JOGO DUROU {diferenca} HORA(S)")

main()
