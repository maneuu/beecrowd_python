def main():
    r, d = 0, 1
    for n in range(1, 40, 2):
        r += n / d
        d *= 2
    print(f"{r:.2f}")

main()
