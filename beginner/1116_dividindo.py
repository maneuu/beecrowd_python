def divisao(X,Y):
    calc = X/Y
    return print(f"{calc:.1f}")

def main():
    repeticoes = int(input())
    for _ in range(repeticoes):
        X, Y = [int(num)for num in input().split()]
        if Y == 0:
            print("divisao impossivel")
        else:
            divisao(X,Y)
main()