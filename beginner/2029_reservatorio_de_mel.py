def main():
    while True:
        try:
            pi = 3.14
            volume = float(input()) # cm ^3
            diametro = float(input()) # cm
            area = pi * (diametro/2)**2
            altura = volume / area
            print(f"ALTURA = {altura:.2f}")
            print(f"AREA = {area:.2f}")
        except EOFError:
            break
main()