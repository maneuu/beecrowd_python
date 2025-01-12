def main():
    quant_pessoas = int(input())
    golpes = [int(num) for num in input().split()]
    print(golpes.index(min(golpes))+1)

main()