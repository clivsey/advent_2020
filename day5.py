import sys

with open("day5_input.txt", "r") as puzzle_input:
  boarding_passes = [line.rstrip() for line in puzzle_input]

def parse_boarding_passes():
  lowest = sys.maxsize
  highest = 0
  seen = set()

  for boarding_pass in boarding_passes:
    min_row, max_row, min_col, max_col = 0, 127, 0, 7
    last_row_dir, last_col_dir = None, None

    for char in boarding_pass:
      if char == "F" or char == "B":
        last_row_dir = char
        if char == "F":
          max_row = max_row - round((max_row - min_row) / 2)
        else:
          min_row = min_row + round((max_row - min_row) / 2)
      elif char == "L" or char == "R":
        last_col_dir = char
        if char == "L":
          max_col = max_col - round((max_col - min_col) / 2)
        else:
          min_col = min_col + round((max_col - min_col) / 2)

    row = min_row if last_row_dir == "F" else max_row
    col = min_col if last_col_dir == "L" else max_col
    boarding_pass_id = row * 8 + col
    seen.add(boarding_pass_id)

    if boarding_pass_id > highest:
      highest = boarding_pass_id
    if boarding_pass_id < lowest:
      lowest = boarding_pass_id

  return lowest, highest, seen

def part1():
  lowest, highest, seen = parse_boarding_passes()
  return highest

def part2():
  lowest, highest, seen = parse_boarding_passes()
  for boarding_pass_id in range(lowest, highest):
    if boarding_pass_id not in seen:
      return boarding_pass_id
  
  return None

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())