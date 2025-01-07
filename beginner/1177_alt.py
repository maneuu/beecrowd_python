def main():
    T = int(input())
    N = [i % T for i in range(1000)]
    for i, x in enumerate(N):
        print(f"N[{i}] = {x}")

main()
