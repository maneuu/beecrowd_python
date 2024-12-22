# Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

viagem_horas = int(input()) #em horas

velocidade_media = int(input()) #em km/h
consumo = 12 # a cada 12km consome um litro de combustível

qts_litros = (velocidade_media * viagem_horas)/ consumo

print(f"{qts_litros:.3f}")