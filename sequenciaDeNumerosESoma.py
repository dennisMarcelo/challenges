""" Leia um número indeterminado de pares de valores M e N (pare quando qualquer um desses valores for menor ou igual a zero). Para cada par, imprima a sequência do menor para o maior (incluindo ambos) e a soma dos inteiros consecutivos entre eles (incluindo ambos).

Entrada
O ficheiro de entrada contém pares de valores inteiros M e N . A última linha do arquivo contém um número zero ou negativo, ou ambos.

Saída
Para cada par de números, imprima a sequência do menor ao maior e a soma desses valores, conforme mostrado abaixo. """

def showResult(a, b):
  pairs = [a, b]
  if( pairs == '' ):
    return ''

  result = ''
  some = 0
  number = pairs[0]
  
  while number <= pairs[1]:
    result = result + str(number) + ' '
    some = some + number
    number = number + 1

  finalResult = result + 'Sum=' + str(some)
  print(finalResult)


def repeate():
  stop = False
  while stop != True:
    paires = input()
    array = paires.split()

    if( int(array[0]) <= 0 or int(array[1]) <= 0):
      break
    
    if( int(array[0]) < int(array[1]) ):
       showResult(int(array[0]), int(array[1]))
    else:
       showResult(int(array[1]), int(array[0]))



repeate()