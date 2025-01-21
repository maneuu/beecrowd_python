def main():
    # Recebe um número em ponto flutuante como entrada
    valor = float(input())
    
    # Formata o número para notação científica usando f-string:
    # - {valor:+.4E} é a f-string que formata o número:
    #   - `+` força a exibição do sinal da mantissa (mostra `+` para positivos e `-` para negativos).
    #   - `.4` define que a mantissa terá exatamente 4 casas decimais.
    #   - `E` converte o número para notação científica com o caractere `E` separando a mantissa do expoente.
    valor = f"{valor:+.4E}"
    
    # Exibe o número formatado
    print(valor)

# Chama a função principal
main()
