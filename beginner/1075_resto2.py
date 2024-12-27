def main():
    N = int(input()) 
    for num in range(1, 10000): 
        if num % N == 2: 
            print(num) 

main()
