def main():
    input()
    total = [int(num) for num in input().split()]
    estrelas = total.copy()
    i = 0
    roubados = 0
    while True:    
        if i > (len(estrelas) - 1) or i < 0: break

        if estrelas[i] > 0:
            roubados += 1
            

        if estrelas[i] % 2 == 0:
            if estrelas[i] > 0:
                estrelas[i] = estrelas[i] - 1
            i -= 1
        else:
            if estrelas[i] > 0:
                estrelas[i] = estrelas[i] - 1
            i += 1
    intersecao = [total[i] for i in range(len(total)) if total[i] == estrelas[i]]
    intersecao = len(intersecao)
    print(f"{len(total) - intersecao} {sum(total) - roubados}")
main()
# 2horas / nivel 7 
