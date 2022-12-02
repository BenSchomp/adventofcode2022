file = open('day-01.txt', 'r')

cur_calories = 0
total_calories = []
for line in file:
  line = line.strip()
  if not line:
    total_calories.append( cur_calories )
    cur_calories = 0
  else:
    cur_calories += int(line)

total_calories.append( cur_calories )
file.close()

total_calories.sort( reverse=True )
print( total_calories[0] )
print( sum(total_calories[:3]) )

