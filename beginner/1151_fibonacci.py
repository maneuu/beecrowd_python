def main():
    N = int(input())
    anterior = 0
    atual = 1

    for _ in range(N):
        if _ == N-1:
            print(anterior)
        else:
            print(anterior, end=" ")
        
        soma = anterior + atual
        anterior = atual
        atual = soma
main()