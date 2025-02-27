minutos_finais = int(input())
valores = [int(n) for n in input().split()]
total = sum(valores)
if total <= minutos_finais:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")