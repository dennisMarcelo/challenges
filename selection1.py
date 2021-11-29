
""" 
Leia 4 valores inteiros A, B, C e D. Então, se B for maior do que C e D for maior do que A e se a soma de C e D for maior do que a soma de A e B e se C e D forem valores positivos e se A for par, escreva a mensagem “Valores aceitos” (Valores aceitos). Caso contrário, escreva a mensagem “Valores nao aceitos” (Valores não aceites).

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostra a mensagem correspondente após a validação dos valores.
 """

inputData = input()
a = int(inputData.split()[0])
b = int(inputData.split()[1])
c = int(inputData.split()[2])
d = int(inputData.split()[3])

condicional1 = b > c
condicional2 = d > a
condicional3 = ( c + d ) > ( a + b )
condicional4 = c > 0
condicional5 = d > 0
condicional6 = a%2 == 0

if condicional1 and condicional2 and condicional3 and condicional4 and condicional5 and condicional6:
  print('Valores aceitos')
else:
  print('Valores nao aceitos')