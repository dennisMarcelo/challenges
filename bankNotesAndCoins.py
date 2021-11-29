""" retorna a quantidade de cedulas e moedas dividi pelo valor  """
notes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print('Digite o valor a ser convertido para moedas e notas:')
value = float(input())

print('NOTAS:')
for note in notes:
  qtdNotes = value/note
  value = float(format((value%note), '.2f'))
  print(int(qtdNotes),'nota(s) de R$', format(note, '.2f'))

print('MOEDAS:')
for coin in coins:
  qtdNotes = value/coin
  value = float(format((value%coin), '.2f'))
  print(int(qtdNotes),'moeda(s) de R$', format(coin, '.2f'))
  