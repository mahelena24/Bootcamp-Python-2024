#Tudo em python é objeto
#Cada objeto tem uma classe e cada classe tem suas características 

# Exercício 1:
try: 
    celsius = float(input("Digite a temperatura em Celsius:"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é de {fahrenheit}")
except ValueError:
    print("Por favor, digite um valor numérico valido")

# Exercício 2:
def verificar_palindromo(letras):
    if isinstance(letras, str):
    
        #removendo espaços e colocando em minúsculo 
        letras = letras.replace(" ", "").lower()  
        #invertendo 
        if letras == letras[::-1]:
           print("É um palíndromo.")
        else:
           print("Não é um palíndromo.")
    else:
        print("Entrada inválida. Por favor, digite uma palavra ou frase.")

try:  
    letras = input("Digite uma palavra ou frase:")
    verificar_palindromo(letras)
except TypeError as e:
    print("Erro:", e)
    
# Exercício 3:
def calculadora(num_1, num_2, op):   
       if op == '+':
           operacao = num_1 + num_2
           print(f"O resultado da operação de {op} será {operacao}")
       elif op == '-':
           operacao = num_1 - num_2
           print(f"O resultado da operação de {op} será {operacao}")
       elif op == '*':
           operacao == num_1 * num_2
           print(f"O resultado da operação de {op} será {operacao}")
       elif op == '/':
           if num_2 != 0:
             operacao == num_1 / num_2
             print(f"O resultado da operação de {op} será {operacao}")
           else:
               print("Divisão por zero. Tente novamente a operação.")
       else:
           print("Operador inválido.")
        
try:
    num_1 = float(input("Digite o primeiro número:"))
    num_2 = float(input("Digite o segundo número:"))
    op = input("Digite o operador desejado:")
    
    calculadora(num_1, num_2, op)
except ValueError:
    print("Erro: Entrada inválida. As entradas devem ser numéricas.")


# Exercício 4:
def classificador_numeros(num1):
        if num1 > 0:
            if num1%2==0:
                print("O número é positivo e par.")
            else:
                print("O número é positivo e impar.")
        elif num1 < 0:
            if num1%2==0:
                print("O número é negativo e par")
            else:
                print("O número é negativo e impar.")
        else:
            print("O número é igual a zero.")

try:      
    num1 = float(input("Digite o número a ser classificado:"))
    classificador_numeros(num1)
except ValueError:
    print("Entrada inválida. Certifique-se que a entrada seja numérica")

# Exercício 5:
