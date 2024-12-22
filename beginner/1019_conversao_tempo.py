# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

segundos_input = int(input(">> "))

horas = int((segundos_input / 60)//60)

minutos = int((segundos_input - (horas * 60 * 60))//60)

segundos = segundos_input % 60
# segundos = segundos_input - (minutos * 60) - (horas * 60**2)

print(f"{horas}:{minutos}:{segundos}")