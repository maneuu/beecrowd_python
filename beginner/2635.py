while True:
    try:
        palavras = []
        for _ in range(int(input())):
            palavras.append(input())
        
        for _ in range(int(input())):
            valor = input()
            count = 0
            maior_palavra = 0
            for palavra in palavras:
                # if valor in palavra:
                if palavra.startswith(valor):  # CORREÇÃO AQUI
                    count += 1
                    if len(palavra) > maior_palavra:
                        maior_palavra = len(palavra)

            if count:
                print(count,maior_palavra)
            else:
                print(-1)
    
    except EOFError:break

                