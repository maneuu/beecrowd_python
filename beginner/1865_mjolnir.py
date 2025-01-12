def main():
    num_casos = int(input())
    for _ in range(num_casos):
        personagem = input().split()
        if "Thor" in personagem:
            print("Y")
        else:
            print("N")
main()