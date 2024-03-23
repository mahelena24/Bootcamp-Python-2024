## Exercitando os tipos de variáveis INT, FLOAT, STRING e BOOLEANO

##################################################################################
### NT
#1-Escreva um programa que soma dois números inteiros inseridos pelo usuário.

num_1 = int(input("Digite o primeiro número:"))
num_2 = int(input("Digite o segundo número:"))
soma = num_1 + num_2
print(f"A soma dos dois números digitados será: {soma}")

#2-Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

num = int(input("Digite o numero desejado:"))
divisor = 5
resto = num%divisor
print(f"O resto da divisao de {num} por {divisor} será igual a {resto}")

#3-Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

num_1 = int(input("Digite o primeiro número:"))
num_2 = int(input("Digite o segundo número:"))
multiplicacao = num_1 * num_2
print(f"A multiplicacao de {num_1} por {num_2} é igual a {multiplicacao}")

#4-Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

num_1 = int(input("Digite o primeiro número:"))
num_2 = int(input("Digite o segundo número:"))

divisao_inteira = int(num_1/num_2)
print(f"A divisao de {num_1} por {num_2} é igual a {divisao_inteira}")

#5-Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num_1 = int(input("Digite o número desejado:"))
quadrado = num_1*num_1
print(f"O quadrado de {num_1} é igual a {quadrado}")

##################################################################################
## Números de Ponto Flutuante (float)
#6-Escreva um programa que receba dois números flutuantes e realize sua adição.

num_1 = float(input("Digite o primeiro número:"))
num_2 = float(input("Digite o segundo número:"))

soma = num_1 + num_2
print(f"A soma de {num_1} e {num_2} é igual a {soma}")

#7-Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num_1 = float(input("Digite o primeiro número:"))
num_2 = float(input("Digite o segundo número:"))
media = (num_1 + num_2)/2
print(f"A média da soma de {num_1} e {num_2} é igual a {media}")

#8-Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
##Relembrando: + (adição) - (subtração) * (multiplicação) / (divisão) ** (potenciação)

base = float(input("Digite a base"))
expoente = float(input("Digite o expoente:"))
potencia = base**expoente
print(f"A potencia de {base} por {expoente} será de {potencia}")

#9-Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius:"))
fahrenheit = (celsius * 9/5) + 32
print(f"Fazendo a conversão, a temperatura ficará igual a {fahrenheit}F")

#10-Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("Digite o raio do seu círculo:"))
pi = 3.14159 
area = pi * raio ** 2
print(f"A area de um circulo de raio igual a {raio} será de {area}")

##################################################################################
### Strings (str)
#11-Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input("Digite um texto: ")
maiuscula = texto.upper()
print(maiuscula)

#12-Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome = input("Digite seu nome completo:")
minuscula = nome.lower()
print(minuscula)

#13-Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite uma frase:")
sem_espaco = frase.strip()
print(sem_espaco)

#14-Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite a data no formado dd/MM/yyyy:")
dia, mes, ano = data.split("/")
print(dia, "\n", mes, "\n", ano)

#15-Escreva um programa que concatene duas strings fornecidas pelo usuário.

string_1 = input("Digite a primeira palavra:")
string_2 = input("Digite a segunda palavra:")

concatenar = string_1 + string_2

##################################################################################
### Booleanos (bool)
#1-Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

express_1 = False
express_2 = False
op = express_1 and express_2
print("O resultado do AND lógico é {op}")

#2-Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

express_1 = False
express_2 = False
op = express_1 or express_2
print("O resultado do OR lógico é {op}")

#3-Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor = False
inverter = not valor 
print(f"O valor de {valor} negado será igual a {inverter}")

#4-Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num_1 = int(input("Digite o primeiro número:"))
num_2 = int(input("Digite o segundo número:"))
resultado = (num_1 == num_2)
print(f"A comparação entre {num_1} e {num_2} de que eles são iguais é {resultado}")

#5-Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num_1 = int(input("Digite o primeiro número:"))
num_2 = int(input("Digite o segundo número:"))
resultado = (num_1 != num_2)
print(f"A comparação entre {num_1} e {num_2} de que eles são diferentes é {resultado}")
