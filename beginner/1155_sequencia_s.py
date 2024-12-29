def main():
    S = 0
    for n in range(1,101):
        S += 1/n
    print(f"{S:.2f}")
main()