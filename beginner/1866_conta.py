def main():
    num_casos = int(input())
    for _ in range(num_casos):
        num_termos = int(input())
        print("0" if num_termos % 2 == 0 else "1")

main()