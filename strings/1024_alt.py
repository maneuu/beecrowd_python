for _ in range(int(input())):
    mensagem = input()

    # Primeira transformação: desloca letras em 3 posições
    mensagem_codificada = [chr(ord(c) + 3) if c.isalpha() else c for c in mensagem]

    # Segunda transformação: Inverte a string
    mensagem_codificada.reverse()

    # Terceira transformação: desloca segunda metade em -1
    metade = len(mensagem) // 2
    for i in range(metade, len(mensagem_codificada)):
        mensagem_codificada[i] = chr(ord(mensagem_codificada[i]) - 1)

    # Converte lista de volta para string e imprime
    print("".join(mensagem_codificada))
