def main():
    i = 0
    while i <= 2:
        for j in range(1,4):
            if i == int(i):
                print(f"I={int(i)} J={int(j+i)}")

            else:
                print(f"I={i:.1f} J={j+i:.1f}")


        i = round(i + 0.2, 1)
main()