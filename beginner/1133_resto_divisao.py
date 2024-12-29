def main():
    X, Y = int(input()), int(input())   
    X, Y = min(X,Y), max(X,Y)

    for num in range(X+1, Y):
        if num % 5 in [2, 3]:
            print(num)

main()