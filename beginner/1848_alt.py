def main():
    valores = {"--*": 1, "-*-": 2, "*--": 4, "-**": 3, "*-*": 5, "**-": 6, "***": 7}
    for _ in range(3):
        soma = 0
        while True:
            entrada = input()
            if entrada == "caw caw":
                break
            soma += valores[entrada]
        print(soma)

main()
