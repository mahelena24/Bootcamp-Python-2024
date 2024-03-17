## Cálculo de Bonus com entrada do usuário

nome = input("Digite o seu nome:")
salario = float(input("Digite o seu salario:"))
porcentagem_bonus = float(input("Digite a porcentagem do seu bonus:"))

calculo_KPI = 1000 + (salario * porcentagem_bonus)
print(f"O usuario {nome} possui o bonus de {calculo_KPI}")
