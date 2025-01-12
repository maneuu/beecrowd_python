def main():
    while True:
        try:
            reclamacoes = input()

            if int(reclamacoes) > 0:
                print("vai ter duas!")
            else:
                print("vai ter copa!")

        except EOFError:
            break

main()
