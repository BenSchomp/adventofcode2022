priorities = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
part_one = part_two = 0
group = [None]*3

file = open('day-03.txt', 'r')

line_count = 0
for line in file:
  line = line.strip()
  line_count += 1

  # --- part one ---
  half = int(len(line)/2)
  for c in line[:half]:
    if c in line[half:]:
      part_one += priorities.find(c)
      break

  # --- part two ---
  g = line_count % 3 # {1,2,0}
  group[g] = line
  if g == 0:
    for c in group[0]:
      if c in group[1] and c in group[2]:
        part_two += priorities.find(c)
        break

file.close()
print( part_one )
print( part_two )
