def main():
    X, Y = map(float, input().split())
    if X == 0 and Y == 0:
        print("Origem")
    elif Y == 0:
        print("Eixo X")
    elif X == 0:
        print("Eixo Y")
    elif X > 0 and Y > 0:
        print("Q1")
    elif X > 0 and Y < 0:
        print("Q4")
    elif X < 0 and Y > 0:
        print("Q2")
    elif X < 0 and Y < 0:
        print("Q3")
main()
