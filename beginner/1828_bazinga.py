def main():
    num_casos = int(input())
    for n in range(1, num_casos + 1):
        sheldon, raj = input().split()

        if sheldon == raj:
            print(f"Caso #{n}: De novo!")

        elif (sheldon == "tesoura" and (raj == "papel" or raj == "lagarto")) or \
             (sheldon == "papel" and (raj == "pedra" or raj == "Spock")) or \
             (sheldon == "pedra" and (raj == "tesoura" or raj == "lagarto")) or \
             (sheldon == "lagarto" and (raj == "Spock" or raj == "papel")) or \
             (sheldon == "Spock" and (raj == "tesoura" or raj == "pedra")):
            print(f"Caso #{n}: Bazinga!")
        else:
            print(f"Caso #{n}: Raj trapaceou!")

main()