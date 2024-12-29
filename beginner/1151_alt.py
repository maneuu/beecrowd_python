def main():
    N = int(input())

    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < N:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    for i in range(N):
        if i == N - 1:
            print(fibonacci_sequence[i])
        else:
            print(fibonacci_sequence[i], end=" ")

main()
