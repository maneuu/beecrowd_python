n = int(input())
h = list(map(int, input().split()))

ok = True
for i in range(1, n - 1):
    if h[i] == h[i-1] or (h[i-1] < h[i] and h[i] < h[i+1]) or (h[i-1] > h[i] and h[i] > h[i+1]):
        ok = False
        break

print(1 if ok else 0)
