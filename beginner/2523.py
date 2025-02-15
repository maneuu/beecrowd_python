while True:
    try:
        string = input()
        N = int(input())
        letras = [int(X) for X in input().split()]
        palavra = ""
        for i in range(N):
            letra = letras[i] - 1
            palavra += string[letra]

        print(palavra)
    except EOFError: break