with open("day10_input.txt", "r") as puzzle_input:
  adapters = sorted((int(line.rstrip()) for line in puzzle_input))

def part1():
  current = 0
  differences = [ 0, 0, 0 ]

  for adapter in adapters:
    diff = adapter - current
    current = adapter
    differences[diff - 1] += 1

  # Device is always +3
  differences[2] += 1

  return differences[0] * differences[2]

def part2():
  num_distinct = dict()
  num_distinct[0] = 1
  
  # Insert starting adapter to count correctly
  adapters.insert(0, 0)
  total_adapters = len(adapters)

  for i, adapter in enumerate(adapters):
    for k in range(i + 1, min(i + 4, total_adapters)):
      next_adapter = adapters[k]
      if next_adapter <= adapter + 3:
        num_distinct[next_adapter] = num_distinct.get(next_adapter, 0) + num_distinct[adapter]

  return num_distinct[adapters[-1]]


print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())