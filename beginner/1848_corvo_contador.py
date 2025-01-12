def main():

    for _ in range(3):
        soma = 0
        while True:
            corvo_input = input()
            if corvo_input == "caw caw": break
            if corvo_input == "--*":
                soma += 1
            elif corvo_input == "-*-":
                soma += 2
            elif corvo_input == "*--":
                soma += 4
            elif corvo_input == "-**":
                soma += 3
            elif corvo_input == "*-*":
                soma += 5
            elif corvo_input == "**-":
                soma += 6
            elif corvo_input == "***":
                soma += 7
        print(soma)

main()