def main():
    i = 0
    while i <= 2:
        for j in range(1, 4):
            print(f"I={i:.0f} J={j + i:.0f}" if i.is_integer() else f"I={i:.1f} J={j + i:.1f}")
        i = round(i + 0.2, 1)

main()
