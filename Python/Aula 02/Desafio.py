# Refatorar o projeto da aula anterior evitando bugs:

#Relembrando: O projeto da aula anterior tem como objetivo calcular o KPI de bÔnus de 2024
# KPI = 1000 + (salario*bonus)

def calculo_kpi(nome, salario, bonus):
    constante = 1000
    KPI = constante + (salario*bonus)
    print(f"{nome}, o KPI de um salário de {salario} e um bonus de {bonus} será de {KPI}")
    
# Verificando o nome digitado 
i = 0; j = 0; k = 0
while i == 0:
 try:
   nome = input("Digite o seu nome:") 
   
   if len(nome) == 0:
       raise ValueError("O nome não pode estar vazio.")
   elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
   else:
       print("Nome válido:", nome)
       i = i+1
 except ValueError as e:
    print(e)

# Verificando o salario digitado
while j ==0:
 try:
    salario = float(input("Digite o seu salário:"))
    
    if salario <0:
        print("Por favor, digite um número maior que zero.")
    else:
        print("Salário válido:", salario)
        j = j+1
 except ValueError:
    print("Entrada inválida para salário. Por favor, digite um valor válido.")
    
# Verificando o bonus digitado
while k == 0:
 try:
    bonus = float(input("Digite o seu bonus recebido:"))
    
    if bonus <0:
        print("Por favor, digite um número maior que zero.")
        bonus = float(input("Digite o seu bonus novamente:")) 
    else:
        print("Bonus válido:", bonus)
        k = k+1 
 except ValueError:
    print("Entrada inválida para bonus. Por favor, digite um valor válido.")

 
# Chamando a função para fazer o cálculo do KPI
calculo_kpi(nome, salario, bonus)