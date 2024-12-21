segundos_input = int(input(">> "))  # Entrada do usuário

# Cálculos otimizados
horas = segundos_input // 3600  # Total de horas
minutos = (segundos_input % 3600) // 60  # Minutos restantes
segundos = segundos_input % 60  # Segundos restantes

# Exibe no formato "HH:MM:SS"
print(f"{horas}:{minutos:02}:{segundos:02}")
