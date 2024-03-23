# Aula 02
 Nessa aula, irei exercitar um pouco mais sobre as variáveis do tipo int, float e booleano. Além disso, irei entender como lidar e trabalhar com erros usando o TypeError, TypeCheck, TypeConversion, TryExcept e IF

## Tipos Primitivos

### Inteiros (int)

1. `+` (adição)
2. `-` (subtração)
3. `*` (multiplicação)
4. `//` (divisão inteira)
5. `%` (módulo - resto da divisão)


### Números de Ponto Flutuante (float)

1. `+` (adição)
2. `-` (subtração)
3. `*` (multiplicação)
4. `/` (divisão)
5. `**`(potenciação)

### Strings (str)

1. `.upper()` (converte para maiúsculas)
2. `.lower()` (converte para minúsculas)
3. `.strip()` (remove espaços em branco no início e no final)
4. `.split(sep)` (divide a string em uma lista, utilizando sep como delimitador)
5. `+` (concatenação de strings)

### Booleanos (bool)

1. `and` (E lógico)
2. `or` (OU lógico)
3. `not` (NÃO lógico)
4. `==` (igualdade)
5. `!=` (diferença)



## Exercícios para treinar:

### Inteiros (int)
1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

### Números de Ponto Flutuante (float)
1. Escreva um programa que receba dois números flutuantes e realize sua adição.
2. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
3. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
4. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
5. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.


### Strings (str)
1. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
2. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
3. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
4. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
5. Escreva um programa que concatene duas strings fornecidas pelo usuário.


### Booleanos (bool)
1. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
2. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
3. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
4. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
5. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.





# TypeError, Type Check e Type Conversion em Python
Python é uma linguagem de programação dinâmica, mas fortemente tipada, o que significa que não é necessário declarar tipos de variáveis explicitamente, mas o tipo de uma variável é determinado pelo valor que ela armazena. Isso introduz a necessidade de compreender como Python lida com diferentes tipos de dados, especialmente quando se trata de operações que envolvem múltiplos tipos. Vamos explorar três conceitos importantes: TypeError, verificação de tipo `(type check)`, e conversão de tipo `(type conversion)`.

## TypeError
Um TypeError ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

### Exemplo de TypeError
Um exemplo clássico é tentar utilizar a função `len()` com um inteiro, o que resulta em TypeError, pois `len()` espera um objeto iterável, como uma string, lista, ou tupla, não um inteiro.

```try:
    resultado = len(5)
    except TypeError as e:
    print(e)  # Imprime a mensagem de erro
```


## Type Conversion
Conversão de tipo `(type conversion)`, também conhecida como casting, é o processo de converter o valor de uma variável de um tipo para outro. Python oferece várias funções integradas para realizar conversões explícitas de tipo, como `int()`, `float()`, `str()`, etc.

### Exemplo de Type Conversion
Se você quiser somar um inteiro e um número flutuante, pode ser necessário converter o inteiro para flutuante ou vice-versa para garantir que a operação de soma seja realizada corretamente.

``` numero_inteiro = 5
    numero_flutuante = 2.5
    #Converte o inteiro para flutuante e realiza a soma
    soma = float(numero_inteiro) + numero_flutuante
    print(soma)  # Resultado: 7.5
```

## Try-Except
A estrutura try-except é usada para tratamento de exceções em Python. Uma exceção é um erro que ocorre durante a execução do programa e que, se não tratado, interrompe o fluxo normal do programa e termina sua execução. O tratamento de exceções permite que o programa lide com erros de maneira elegante, permitindo que continue a execução ou falhe de forma controlada.

try: Este bloco é o primeiro na estrutura de tratamento de exceções. Python tenta executar o código dentro deste bloco.
except: Se uma exceção ocorrer no bloco try, a execução imediatamente salta para o bloco except. Você pode especificar tipos de exceção específicos para capturar e tratar apenas essas exceções. Se nenhum tipo de exceção for especificado, ele captura todas as exceções.

```try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
    except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")
```

## Exercícios 

### 1. Conversor de temperatura
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando `try-except`, garantir que a entrada seja numérica, tratando qualquer `ValueError`. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

### 2. Verificador de Palíndromo
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize `try-except` para garantir que a entrada seja uma string. Dica: Utilize a função `isinstance()` para verificar o tipo da entrada.

### 3. Calculadora Simples
Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use `try-except` para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

### 4. Classificador de Números
Escreva um programa que solicite ao usuário para digitar um número. Utilize `try-except` para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

### 5. Classificador de Números 
Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize `try-except` para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.