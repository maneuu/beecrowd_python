for _ in range(int(input())):
    mensagem_codificada = ""
    mensagem_original = input()

    # Primeira transformação: desloca letras em 3 posições
    for caractere in mensagem_original:
        if caractere.isalpha():
            mensagem_codificada += chr(ord(caractere) + 3)
        else:
            mensagem_codificada += caractere

    # Segunda transformação: Inverte a string
    mensagem_codificada = mensagem_codificada[::-1]

    # Terceira transformação: desloca segunda metade em -1
    metade_indice = len(mensagem_original) // 2
    mensagem_final = mensagem_codificada[:metade_indice]

    for indice in range(metade_indice, len(mensagem_original)):
        mensagem_final += chr(ord(mensagem_codificada[indice]) - 1)

    print(mensagem_final)
