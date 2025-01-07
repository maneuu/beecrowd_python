def main():
    fibonacci = [0,1]
    for i in range(60):
        fibonacci.append(fibonacci[-2] + fibonacci [-1])
    num_casos = int(input())
    for _ in range(num_casos):
        posicao = int(input())
        print(f"Fib({posicao}) = {fibonacci[posicao]}")
main()