def main():
    while True:
        try:
            hora, minuto = [int(num) for num in input().split(":")]
            total = hora * 60 + minuto  # Converte o horário para minutos
            encontro = 8 * 60  # 8h em minutos (480 minutos)
            
            # Calcula o atraso máximo
            atraso_maximo = encontro - total - 60
            print(f"Atraso maximo: {abs(atraso_maximo) if atraso_maximo < 0 else 0}")
        except EOFError:
            break

main()
