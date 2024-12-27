def main():
    repeticoes = int(input())

    for _ in range(repeticoes):
        valores = input().split()
        num1, num2, num3 = [float(x) for x in valores]
        media = (num1 * 2 + num2 * 3 + num3 * 5)/10
        print(f"{media:.1f}")
main()