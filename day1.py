with open("day1_input.txt", "r") as puzzle_input:
  expenses = sorted([int(line) for line in puzzle_input])

def part1():
  seen = set()
  for expense in expenses:
    pair = 2020 - expense
    if pair in seen:
      return pair * expense
    seen.add(expense)

  return 0

def part2():
  total = len(expenses)
  for left in range(total):
    mid = left + 1
    right = total - 1
    while left < right:
      sum = expenses[left] + expenses[mid] + expenses[right]
      if sum > 2020: right -= 1
      elif sum < 2020: left += 1
      else: return expenses[left] * expenses[mid] * expenses[right]

  return 0

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())