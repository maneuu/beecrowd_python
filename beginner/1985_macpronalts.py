def main():
    cardapio = {
        # codigo : valor
        1001 : 1.50,
        1002 : 2.50,
        1003 : 3.50,
        1004 : 4.50,
        1005 : 5.50, 
    }
    num_casos = int(input())
    valor_final = 0
    for _ in range(num_casos):
        codigo, quantidade = [int(num) for num in input().split()]
        valor_final += cardapio[codigo] * quantidade
    print(f"{valor_final:.2f}")

main()
