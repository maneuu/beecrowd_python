def main():
    numero = int(input())
    for num in range(2,numero+1,2):
        print(f"{num} ^ 2 = {num**2}")

main()