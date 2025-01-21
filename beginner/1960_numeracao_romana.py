def int_to_roman(num):
    # Mapeamento de valores inteiros para números romanos
    roman_numerals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = ""
    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value
    return result

def main():
    numero = int(input())
    print(f"{int_to_roman(numero)}")
main()