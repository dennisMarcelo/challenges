""" A long time ago, in a galaxy far, far away...

After the decline of the Empire, scavengers are spread around the universe looking for a lost lightsaber. Everyone knows that a lightsaber emits an unique wave pattern: 42 surrounded by 7 all around. You have a wave sensor that scans a terrain with N x M cells. Look at the example below for an 4 x 7 terrain with a lightsaber in it (at position (2,4)).

 

You must write a program that, given an N x M terrain, looks for the lightsaber pattern in it. No scan have more than one lightsaber pattern.

Input
The first line of the input has two positive integers N and M, representing respectively the number of rows and the number of columns scanned in a terrain (3 ≤ N, M ≤ 1000). Each of the next N lines have M integers, describing the values scanned in each cell of the terrain (-100 ≤ Tij ≤ 100, for 1 ≤ i ≤ N and 1 ≤ j ≤ M).

Output
The output is a single line with 2 integers X and Y separated by one space. They represent the (X,Y)-coordinate of the lightsaber, if it is found. If the terrain doesn't have a lightsaber pattern, X and Y are both zero. """

def getMap(lines):
  m = []
  counter = 0
  
  while counter < lines:
    line = input().split()
    lineParsedToInt = []
    for number in line:
      lineParsedToInt.append(int(number))

    m.append(lineParsedToInt)
    counter += 1

  return m

def toScanMap(lines, columns, map):
  position = ''
  for line in range(1, lines-1):
    for column in range(1, columns-1):
      if map[line][column] == 42:
        if map[line-1][column-1] == 7 and map[line -1][column] == 7 and map[line -1][column+1] == 7:
          if map[line][column -1] == 7 and map[line][column + 1] == 7:
            if map[line +1][column-1] == 7 and map[line -1][column] == 7 and map[line +1][column + 1] == 7:
              position = '{} {}'.format(line+1, column+1)
              break

  if position == '':
    return '0 0'
  
  return position

lc = input().split()
l, c = int(lc[0]), int(lc[1])

map = getMap(l)
position = toScanMap(l, c, map)


print('---------Sabre position-----------')
print(position)