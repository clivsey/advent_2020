with open("day15_input.txt", "r") as puzzle_input:
  starting_numbers = [int(num) for line in puzzle_input for num in line.rstrip().split(",")]

def get_num_history(num, history, round):
  num_history = history.get(num, None)
  if num_history == None:
    num_history = [round, round]
    history[num] = num_history
  else:
    num_history[0] = num_history[1]
    num_history[1] = round
    
  return num_history

def memory_game(max_rounds):
  history = dict()
  round = 0
  last_num = 0

  for starting_number in starting_numbers:
    round += 1
    last_num = starting_number
    last_num_history = get_num_history(starting_number, history, round)

  while round < max_rounds:
    num_history = get_num_history(last_num, history, round)
    round += 1
    if num_history[0] == num_history[1]:
      last_num = 0
    else:
      last_num = num_history[1] - num_history[0]

  return last_num

def part1():
  return memory_game(2020)

def part2():
  return memory_game(30000000)

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())