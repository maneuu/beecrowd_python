def main():
    dic_hex = {
        10 : "A",
        11 : "B",
        12 : "C",
        13 : "D",
        14 : "E",
        15 : "F"
    }
    hexadecimal = []
    valor = int(input())
    if valor > 15:
        while True:
            if valor == 0: break
            hexadecimal.append(valor % 16)
            valor = int(valor/16)
        hexadecimal.reverse()
        resultado = ""
        for num in hexadecimal:
            if num in dic_hex:
                resultado += f"{dic_hex[num]}"
            else:
                resultado += f"{num}"
        print(resultado)
    else:
        if valor in dic_hex:
            print(dic_hex[valor])
        else:
            print(valor)
main()
