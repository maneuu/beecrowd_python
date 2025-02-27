from math import sqrt
magias = {
    "fire": {1: 20, 2: 30, 3: 50},
    "water": {1: 10, 2: 25, 3: 40},
    "earth": {1: 25, 2: 55, 3: 70},
    "air": {1: 18, 2: 38, 3: 60}
}

danos = {
    "fire": 200,
    "water": 300,
    "earth": 400,
    "air": 100
}

for _ in range(int(input())):

    w,h,x0,y0 = [int(X) for X in input().split()]
    magia, nivel , cx, cy = input().split()
    nivel = int(nivel)
    cx, cy = int(cx), int(cy)
    
    # Acessando o raio da magia no nível desejado
    raio = magias[magia][nivel]
    
    # Acessando o dano da magia
    dano = danos[magia]

    # Encontrar o ponto mais próximo do retângulo em relação ao centro da explosão
    px = max(x0, min(cx, x0 + w))
    py = max(y0, min(cy, y0 + h))

    # Calcular a distância entre o centro da explosão e o ponto mais próximo
    distancia = sqrt((cx - px)**2 + (cy - py)**2)

    # Verificar se a distância é menor ou igual ao raio
    if distancia <= raio:
        print(dano)
    else:
        print(0)