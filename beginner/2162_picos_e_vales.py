n = int(input())
h = list(map(int, input().split()))

ok = True
for i in range(1, n):
    if h[i] == h[i-1]:  # Checa valores consecutivos iguais
        ok = False
        break
    if i > 1:  # Verifica alternância a partir do terceiro valor
        if (h[i-1] > h[i-2] and h[i] >= h[i-1]) or (h[i-1] < h[i-2] and h[i] <= h[i-1]):
            ok = False
            break

print(1 if ok else 0)
