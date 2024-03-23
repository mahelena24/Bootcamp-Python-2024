# Aula 02
 Nessa aula, irei exercitar um pouco mais sobre as variáveis do tipo int, float e booleano. Além disso, irei entender como lidar e trabalhar com erros usando o TypeError, TypeCheck, TypeConversion, TryExcept e IF

## Tipos Primitivos
1. Inteiros (int)
Métodos e operações:
"+" (adição)
"-" (subtração)
* (multiplicação)
// (divisão inteira)
% (módulo - resto da divisão)

2. Números de Ponto Flutuante (float)
Métodos e operações:
+ (adição)
- (subtração)
* (multiplicação)
/ (divisão)
** (potenciação)

3. Strings (str)
Métodos e operações:
.upper() (converte para maiúsculas)
.lower() (converte para minúsculas)
.strip() (remove espaços em branco no início e no final)
.split(sep) (divide a string em uma lista, utilizando sep como delimitador)
+ (concatenação de strings)
4. Booleanos (bool)
Operações lógicas:
and (E lógico)
or (OU lógico)
not (NÃO lógico)
== (igualdade)
!= (diferença)



## Exercícios para treinar:

### Inteiros (int)
1-Escreva um programa que soma dois números inteiros inseridos pelo usuário.
2-Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
3-Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
4-Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
5-Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

### Números de Ponto Flutuante (float)
1-Escreva um programa que receba dois números flutuantes e realize sua adição.
2-Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
3-Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
4-Faça um programa que converta a temperatura de Celsius para Fahrenheit.
5-Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.


### Strings (str)
1-Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
2-Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
3-Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
4-Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
5-Escreva um programa que concatene duas strings fornecidas pelo usuário.


### Booleanos (bool)
1-Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
2-Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
3-Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
4-Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
5-Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.



# TypeError, Type Check e Type Conversion em Python
Python é uma linguagem de programação dinâmica, mas fortemente tipada, o que significa que não é necessário declarar tipos de variáveis explicitamente, mas o tipo de uma variável é determinado pelo valor que ela armazena. Isso introduz a necessidade de compreender como Python lida com diferentes tipos de dados, especialmente quando se trata de operações que envolvem múltiplos tipos. Vamos explorar três conceitos importantes: TypeError, verificação de tipo (type check), e conversão de tipo (type conversion).

## TypeError
Um TypeError ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

### Exemplo de TypeError
Um exemplo clássico é tentar utilizar a função len() com um inteiro, o que resulta em TypeError, pois len() espera um objeto iterável, como uma string, lista, ou tupla, não um inteiro.

# Exemplo que causa TypeError
"try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro"



## Type Conversion
Conversão de tipo (type conversion), também conhecida como casting, é o processo de converter o valor de uma variável de um tipo para outro. Python oferece várias funções integradas para realizar conversões explícitas de tipo, como int(), float(), str(), etc.

### Exemplo de Type Conversion
Se você quiser somar um inteiro e um número flutuante, pode ser necessário converter o inteiro para flutuante ou vice-versa para garantir que a operação de soma seja realizada corretamente.

"numero_inteiro = 5
numero_flutuante = 2.5
 #Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5"

## Try-Except
A estrutura try-except é usada para tratamento de exceções em Python. Uma exceção é um erro que ocorre durante a execução do programa e que, se não tratado, interrompe o fluxo normal do programa e termina sua execução. O tratamento de exceções permite que o programa lide com erros de maneira elegante, permitindo que continue a execução ou falhe de forma controlada.

try: Este bloco é o primeiro na estrutura de tratamento de exceções. Python tenta executar o código dentro deste bloco.
except: Se uma exceção ocorrer no bloco try, a execução imediatamente salta para o bloco except. Você pode especificar tipos de exceção específicos para capturar e tratar apenas essas exceções. Se nenhum tipo de exceção for especificado, ele captura todas as exceções.

### Exemplo de try-except
"try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")
"

