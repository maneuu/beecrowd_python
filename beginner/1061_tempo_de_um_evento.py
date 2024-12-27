def main():
    # Captura os dados de entrada
    dia_i = int(input().split()[1])
    hora_i, minuto_i, segundo_i = map(int, input().split(" : "))
    dia_f = int(input().split()[1])
    hora_f, minuto_f, segundo_f = map(int, input().split(" : "))

    # Converte o início e fim para segundos totais
    total_segundos_i = dia_i * 86400 + hora_i * 3600 + minuto_i * 60 + segundo_i
    total_segundos_f = dia_f * 86400 + hora_f * 3600 + minuto_f * 60 + segundo_f

    # Calcula a diferença em segundos
    diferenca_total = total_segundos_f - total_segundos_i

    # Converte de volta para dias, horas, minutos e segundos
    diferenca_dia = diferenca_total // 86400

    diferenca_total %= 86400 #

    diferenca_hora = diferenca_total // 3600

    diferenca_total %= 3600

    diferenca_minuto = diferenca_total // 60
    diferenca_segundo = diferenca_total % 60

    # Imprime a saída no formato especificado
    print(f"{diferenca_dia} dia(s)")
    print(f"{diferenca_hora} hora(s)")
    print(f"{diferenca_minuto} minuto(s)")
    print(f"{diferenca_segundo} segundo(s)")

main()
