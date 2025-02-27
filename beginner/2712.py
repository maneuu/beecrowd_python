casos = int(input())

regras = {
    1: "MONDAY", 2: "MONDAY",
    3: "TUESDAY", 4: "TUESDAY",
    5: "WEDNESDAY", 6: "WEDNESDAY",
    7: "THURSDAY", 8: "THURSDAY",
    9: "FRIDAY", 0: "FRIDAY"
}

for _ in range(casos):
    placa = input().strip()

    if (
        (sum(c.isalpha() for c in placa) != 3) or
        (sum(c.isdigit() for c in placa) != 4) or
        (len(placa) != 8) or
        (placa[3] != '-') or
        (not placa.isupper())
    ):
        print("FAILURE")
    else:
        print(regras[int(placa[-1])])
