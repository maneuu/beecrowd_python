def main():
    p,j1,j2,r,a = [int(num) for num in input().split()]
    

    if bool(r):
        if bool(a):
            print("Jogador 2 ganha!")
        else:
            print("Jogador 1 ganha!")
    else:
        soma = j1 + j2
        if (soma % 2 == 0 and p == 1) or (soma % 2 == 1 and p == 0):
            print("Jogador 1 ganha!")  
        else:
            print("Jogador 2 ganha!")
main()