def main():
    p,j1,j2,r,a = [int(num) for num in input().split()]
    

    if bool(r):
        if bool(a):
            print("Jogador 2 ganha!")
        else:
            print("Jogador 1 ganha!")
    else:
        soma = j1 + j2
        if bool(p):
            #J1 é par e j2 impar
            if soma % 2 == 0:
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")
        else:
            #J1 é impar e J2 par
            if soma % 2 == 0:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
main()