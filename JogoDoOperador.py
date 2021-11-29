""" Samu Elmito loves creating peculiar games to challenge his friends. This time, he made a game called "Jogo do Operador" (Operation Game), in which he creates basic expresssions and each player must choose an expression and fill the gap with the correct operation to validate it. The players may choose 1 out of 3 operations: addition, subtraction and multiplication. However, if the player thinks there's no operation among the 3 operations that validates the expression, he can anwser Impossible.

Your task is simple: given the expressions and the players' answer, determine which players won't proceed to the next phase of the game.

Input
The input consists of an integer T (2 ≤ T ≤ 50) that indicates the number of expression and the number of players. Each test case consists of T expressions like "X Y=Z", indicating that X operation Y (0 ≤ X, Y ≤ 103) is equal to Z (-103 ≤ Z ≤ 106), followed by T players and his respective answers like "N E R", with N being the player's name (up to 50 characters and no blank spaces), E being the index of the chosen expression (1 ≤ E ≤ T) and R the answer (+, -, * or I, indicating Impossible). Read input until EOF.

Output
For each test case, if every player can proceed, print "You Shall All Pass!"; if no player can proceed, print "None Shall Pass!"; otherwise, print, in lexicographical order and between blank spaces, the name of the players who gave the wrong answer and won't proceed to the next phase. """

def getExpressions(qtdExp):
  expressions = []
  count = 0
  while count < qtdExp:
    inp = input().replace('=', ' ').split()
    num1 = int(inp[0])
    num2 = int(inp[1])
    result = int(inp[2])
    expressions.append([num1, num2, result])
    
    count+=1

  return expressions

def getUserGames(qtdExp):
  game = []
  count = 0
  while count < qtdExp:
    inp = input().split()
    name = inp[0]
    indice = int(inp[1])
    expression = inp[2]
    game.append([name, indice, expression])

    count+=1
  return game

def getLosers(expressions, userGames):
  losers = []
  for game in userGames:
    expr = expressions[game[1]-1]

    if(game[2] != 'I'):
      resultUser = eval('{} {} {}'.format(expr[0], game[2], expr[1]))

      if(resultUser != expr[2]):
        losers.append(game[0])
        
    
    test1 = eval('{} {} {}'.format(expr[0], '*', expr[1]))
    test2 = eval('{} {} {}'.format(expr[0], '+', expr[1]))
    test3 = eval('{} {} {}'.format(expr[0], '-', expr[1]))
    if(game[2] == 'I'):
      if(expr[2]==test1 or expr[2]==test2 or expr[2]==test3):
        losers.append(game[0])

  return sorted(losers)

while True:
  try:
    qtdExp = int(input())
    expressions = getExpressions(qtdExp)
    userGames = getUserGames(qtdExp)
    losers = getLosers(expressions, userGames)

    if(len(losers) == qtdExp):
      print('None Shall Pass!')
    elif(len(losers) == 0):
      print('You Shall All Pass!')
    else:
      print(' '.join(map(str, losers)))
  except:
    break

""" 
tests
3
8 4=5
2 5=5
1 3=4
Samuel 2 +
Abner 3 +
Aline 1 *

3
8 4=5
2 5=5
1 3=4
Samuel 2 I
Abner 3 +
Aline 1 I

3
8 4=5
2 5=5
1 3=4
Samuel 2 -
Abner 3 I
Aline 1 +

3
8 4 = 5
2 5 = 5
1 3 = 4
Samuel 2 +
Abner 3 +
Aline 1 *
2
1 2 = -1
0 7 = 7
Luiz 2 -
Absolut 1 +

 """