def main():
    num_casos = int(input())
    for _ in range(num_casos):
        informacoes = input().split()
        dic_info = {
            informacoes[1] : informacoes[0],
            informacoes[3] : informacoes[2]
            }

        P1, P2 = [int(num) for num in input().split()]
        if (P1 + P2) % 2 == 0:#PAR
            print(dic_info["PAR"])
        else:
            print(dic_info["IMPAR"])
main()