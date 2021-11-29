inputValue = float(input())

def interval(value):
  if(value < 0 or value > 100):
    return 'Fora de intervalo'
  
  if(value >= 0 and value <= 25):
    return 'Intervalo [0,25]'

  if(value > 25 and value <= 50):
    return 'Intervalo (25,50]'

  if(value > 50 and value <= 75):
    return 'Intervalo (50,75]'
  
  if(value > 75 and value <= 100):
    return 'Intervalo (75,100]'

print(interval(inputValue))