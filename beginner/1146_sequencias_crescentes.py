def main():
    while True:
        X = int(input())
        if X == 0:
            break

        for num in range(1,X+1):
            if num == X:
                print(num)
            else:
                print(num, end=" ")
        
main()