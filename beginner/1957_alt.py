def main():
    # Solicita um número decimal ao usuário
    numero_decimal = int(input("Digite um número decimal: "))
    
    # Converte o número para hexadecimal, remove o prefixo '0x' e transforma em maiúsculas
    resultado_hexadecimal = hex(numero_decimal)[2:].upper()
    
    # Exibe o resultado em formato hexadecimal
    print(f"Hexadecimal: {resultado_hexadecimal}")

main()
