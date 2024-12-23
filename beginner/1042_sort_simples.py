"""Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
"""

def main():
    num1, num2, num3 = map(int, input().split())
    ordem_crescente = [num1, num2, num3]
    ordem_crescente.sort()
    for num in ordem_crescente:
        print(num)
    print()
    print(f"{num1}\n{num2}\n{num3}")
    
main()