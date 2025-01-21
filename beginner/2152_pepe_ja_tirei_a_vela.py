casos = int(input())
for _ in range(casos):
    h, m, porta = [int(num) for num in input().split()]
    hora_formatada = f"{h:02}:{m:02}"
    print(f"{hora_formatada} - A porta {'abriu' if porta else 'fechou'}!")