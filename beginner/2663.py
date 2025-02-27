num_competidores = int(input())  
min_classificados = int(input())  
pontuacoes = []  

for _ in range(num_competidores):  
    pontuacoes.append(int(input()))  

pontuacoes.sort(reverse=True)  

total_classificados = min_classificados  

for i in range(min_classificados, len(pontuacoes)):  
    if pontuacoes[min_classificados - 1] == pontuacoes[i]:  
        total_classificados += 1  

print(total_classificados)  
