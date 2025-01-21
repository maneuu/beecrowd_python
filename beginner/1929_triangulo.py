def pode_formar_triangulo(a, b, c, d):
    return (
        (a + b > c and a + c > b and b + c > a) or  # Combinação (a, b, c)
        (a + b > d and a + d > b and b + d > a) or  # Combinação (a, b, d)
        (a + c > d and a + d > c and c + d > a) or  # Combinação (a, c, d)
        (b + c > d and b + d > c and c + d > b)     # Combinação (b, c, d)
    )

def main():
    A,B,C,D = [int(num) for num in input().split()]

    if pode_formar_triangulo(A, B, C, D):
        print("S") # É possível formar um triângulo.
    else:
        print("N") # Não é possível formar um triângulo.
main()