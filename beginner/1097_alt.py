def main():
    j_start = 7
    
    for i in range(1, 10, 2):  # `i` varia de 1 a 9, pulando de 2 em 2
        for j in range(j_start, j_start - 3, -1):  # `j` varia começando de `j_start` e decrementando
            print(f"I={i} J={j}")
        j_start += 2  # Incrementa o início de `J` a cada nova iteração de `I`
main()
