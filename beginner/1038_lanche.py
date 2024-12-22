"""Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal."""

codigo_preco = {
    # CODIGO: PREÇO
    "1": 4,#Cachorro Quente
    "2": 4.5,#X-Salada
    "3": 5,#X-Bacon
    "4": 2,#Torrada Simples
    "5": 1.5#Refrigerante
}
def main():
    valores = input().split()
    lanche_codigo, quantidade = valores[0], int(valores[1])
    total = codigo_preco[lanche_codigo] * quantidade
    print(f"Total: R$ {total:.2f}")

main()