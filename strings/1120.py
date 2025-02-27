while True:
    digito_erro, valor_entrada = input().split()
    if digito_erro == "0" and valor_entrada == "0":
        break 

    mensagem_final = valor_entrada.replace(digito_erro, "")
    if mensagem_final == "":
        mensagem_final = 0

    print(int(mensagem_final) * 1)