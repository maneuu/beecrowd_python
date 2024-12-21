employee_id = int(input("Digite o ID do funcionário: "))
hours_worked = int(input("Digite o número de horas trabalhadas: "))
hourly_rate = float(input("Digite o valor do pagamento por hora: "))

salary = hourly_rate * hours_worked
print(f"NUMBER = {employee_id}")
print(f"SALARY = U$ {salary:.2f}")