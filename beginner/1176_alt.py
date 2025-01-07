def main():
    fibonacci = [0, 1]
    for _ in range(2, 61):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    for _ in range(int(input())):
        n = int(input())
        print(f"Fib({n}) = {fibonacci[n]}")

main()
