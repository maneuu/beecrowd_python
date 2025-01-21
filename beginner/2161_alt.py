N = int(input())

denominador = 0
for _ in range(N):
    denominador = 1 / (6 + denominador)

formula = 3 + denominador
print(f"{formula:.10f}")
