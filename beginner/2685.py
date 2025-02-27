while True:
    try:
            
        angulo = int(input())

        if (0 <= angulo < 90) or angulo == 360:
            print("Bom Dia!!")
        elif 90 <= angulo < 180:
            print("Boa Tarde!!")
        elif 180 <= angulo < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")
    except EOFError: break