n = int(input())
for _ in range(n):
    b = int(input())
    d_a, d_d, d_l = map(int, input().split())
    g_a, g_d, g_l = map(int, input().split())

    d_valor = (d_a + d_d) / 2 + (b if d_l % 2 == 0 else 0)
    g_valor = (g_a + g_d) / 2 + (b if g_l % 2 == 0 else 0)

    if d_valor > g_valor:
        print("Dabriel")
    elif g_valor > d_valor:
        print("Guarte")
    else:
        print("Empate")
