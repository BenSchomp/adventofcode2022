file = open('day-01.txt', 'r')
data = []

calories = 0
max_calories = None
for line in file:
  line = line.strip()
  if not line:
    if not max_calories or calories > max_calories:
      max_calories = calories
    calories = 0
  else:
    calories += int( line.strip() )
file.close()

if calories > max_calories:
  max_calories = calories

print( max_calories )