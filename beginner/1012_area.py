valores = input().split()

valor_a = float(valores[0]) 
valor_b = float(valores[1])
valor_c = float(valores[2]) 

pi = 3.14159

triangulo = (valor_a * valor_c)/2 
circulo = pi * valor_c **2
trapezio = (valor_a + valor_b) * valor_c / 2
quadrado = valor_b ** 2
retangulo = valor_a * valor_b

print(f'''TRIANGULO: {triangulo:.3f}
CIRCULO: {circulo:.3f}
TRAPEZIO: {trapezio:.3f}
QUADRADO: {quadrado:.3f}
RETANGULO: {retangulo:.3f}''')