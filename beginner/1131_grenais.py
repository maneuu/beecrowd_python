def main():
    grenais_info = {"Grenais": 0, "Inter": 0, "Gremio": 0, "Empates": 0}

    while True:
        grenais_info["Grenais"] += 1

        # Entrada de gols
        inter_gols, gremio_gols = map(int, input().split())

        # Atualização de resultados
        if gremio_gols > inter_gols:
            grenais_info["Gremio"] += 1
        elif gremio_gols < inter_gols:
            grenais_info["Inter"] += 1
        else:
            grenais_info["Empates"] += 1

        # Pergunta para continuar
        while True:
            repetir = int(input("Novo grenal (1-sim 2-nao)\n"))
            if repetir in [1, 2]:
                break

        if repetir == 2:
            # Exibição dos resultados finais
            print(f"{grenais_info['Grenais']} grenais")
            print(f"Inter:{grenais_info['Inter']}")
            print(f"Gremio:{grenais_info['Gremio']}")
            print(f"Empates:{grenais_info['Empates']}")

            if grenais_info["Gremio"] > grenais_info["Inter"]:
                maior_vencedor = "Gremio venceu mais"
            elif grenais_info["Gremio"] < grenais_info["Inter"]:
                maior_vencedor = "Inter venceu mais"
            else:
                maior_vencedor = "Não houve vencedor"
            
            print(maior_vencedor)
            break

main()