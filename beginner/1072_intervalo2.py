def main():
    repeticoes = int(input())
    dentro = fora = 0
    for _ in range(repeticoes):
        num = int(input())
        if num >= 10 and num <= 20:
            dentro += 1
        else:
            fora += 1
    print(f"{dentro} in")
    print(f"{fora} out")
main()