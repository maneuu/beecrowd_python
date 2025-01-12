def main():
    # Mapeamento de condições de vitória
    regras = {
        "tesoura": ["papel", "lagarto"],
        "papel": ["pedra", "Spock"],
        "pedra": ["tesoura", "lagarto"],
        "lagarto": ["Spock", "papel"],
        "Spock": ["tesoura", "pedra"]
    }

    num_casos = int(input())
    for n in range(1, num_casos + 1):
        sheldon, raj = input().split()

        if sheldon == raj:
            print(f"Caso #{n}: De novo!")
        elif raj in regras[sheldon]:
            print(f"Caso #{n}: Bazinga!")
        else:
            print(f"Caso #{n}: Raj trapaceou!")

main()
