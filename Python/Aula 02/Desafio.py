# Refatorar o projeto da aula anterior evitando bugs:

#Relembrando: O projeto da aula anterior tem como objetivo calcular o KPI de bÔnus de 2024
# KPI = 1000 + (salario*bonus)

def calculo_kpi(nome, salario, bonus):
    constante = 1000
    KPI = constante + (salario*bonus)
    print(f"{nome}, o KPI de um salário de {salario} e um bonus de {bonus} será de {KPI}")
    