def part1():
  result = 0

  groups = list()
  group_set = set()
  with open("day6_input.txt", "r") as puzzle_input:
    for line in puzzle_input:
      line = line.rstrip()
      if line == "":
        groups.append(group_set)
        group_set = set()
      else:
        group_set.update([char for char in line])

    # Add the last one in the event there is not a line break at the end
    if len(group_set) > 0:
      groups.append(group_set)
      
  for group_set in groups:
    result += len(group_set)

  return result

def part2():
  result = 0

  groups = list()
  group_set = set()

  # Bool to track first in group because we can't rely on len of 0 alone because
  # there might be groups that not everyone answered "yes" to all before the last response
  first_in_group = True

  with open("day6_input.txt", "r") as puzzle_input:
    for line in puzzle_input:
      line = line.rstrip()
      if line == "":
        groups.append(group_set)
        group_set = set()
        first_in_group = True
      else:
        if first_in_group:
          group_set.update([char for char in line])
        else:
          group_set = group_set.intersection([char for char in line])

        first_in_group = False

    # Add the last one in the event there is not a line break at the end
    if len(group_set) > 0:
      groups.append(group_set)
      
  for group_set in groups:
    result += len(group_set)

  return result

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())