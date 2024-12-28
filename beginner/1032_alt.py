def soma_sem_multiplos_de_13(x, y):
    return sum(num for num in range(min(x, y), max(x, y) + 1) if num % 13 != 0)

def main():
    x = int(input())
    y = int(input())
    print(soma_sem_multiplos_de_13(x, y))

main()
