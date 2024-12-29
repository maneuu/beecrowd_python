def main():
    A, N = [int(num) for num in input().split() if int(num) > 0]
    while N <= 0:
        N = int(input())
    soma = 0
    for i in range(0,N):
        soma += A + i
    print(soma)
main()