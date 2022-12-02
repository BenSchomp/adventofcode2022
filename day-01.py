file = open('day-01.txt', 'r')
data = []
for line in file:
  line = line.strip()
  if not line:
    data.append( None )
  else:
    data.append( int(line) )
file.close()

def part_one():
  calories = 0
  max_calories = 0
  for cur in data:
    if not cur:
      calories = 0
    else:
      calories += cur

    if calories > max_calories:
      max_calories = calories

  print( max_calories )

def part_two():
  calories = 0
  total_calories = []
  for cur in data:
    if not cur:
      total_calories.append( calories )
      calories = 0
    else:
      calories += cur

  total_calories.append( calories )
  total_calories.sort(reverse=True)

  print( sum(total_calories[:3]) )

part_one()
part_two()
