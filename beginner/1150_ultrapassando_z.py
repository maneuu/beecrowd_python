def main():
    X = int(input())
    Z = int(input())
    while Z <= X:
        Z = int(input())
        
    soma, i = 0, 0
    while soma <= Z:
        soma += X + i
        i += 1
    print(i)

main()