while True:
    try:
        angulo = float(input())
        
        # Saudação baseada no ângulo
        if (0 <= angulo < 90) or angulo == 360:
            print("Bom Dia!!")
        elif 90 <= angulo < 180:
            print("Boa Tarde!!")
        elif 180 <= angulo < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")
        
        # Conversão do ângulo para tempo (HH:MM:SS)
        # Considera que 360° correspondem a 24h e que 0° corresponde a 06:00:00.
        total_horas = (angulo / 15) + 6
        total_horas %= 24  # Ajusta caso ultrapasse 24h
        
        # Converte as horas totais para segundos e arredonda
        total_segundos = round(total_horas * 3600)
        
        horas = total_segundos // 3600
        minutos = (total_segundos % 3600) // 60
        segundos = total_segundos % 60
        
        print(f"{horas:02}:{minutos:02}:{segundos:02}")
        
    except EOFError:
        break
