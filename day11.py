from copy import deepcopy

with open("day11_input.txt", "r") as puzzle_input:
  seating_grid = [[char for char in line.rstrip()] for line in puzzle_input]

rows = len(seating_grid)
cols = len(seating_grid[0])

def count_occupied_seats(grid, row, col):
  occupied_seats = 0
  for i in range(max(row - 1, 0), min(row + 2, rows)):
    for k in range(max(col - 1, 0), min(col + 2, cols)):
      # Make sure to not count the current seat
      if i != row or k != col:
        if grid[i][k] == "#":
          occupied_seats += 1

  return occupied_seats

def count_occupied_seats_direction(grid, row, col):
  occupied_seats = 0
  for row_dir in range(-1, 2):
    for col_dir in range(-1, 2):
      # Make sure to not count the current seat, as well as avoid an infinite loop below
      if row_dir != 0 or col_dir != 0:
        curr_row = row + row_dir
        curr_col = col + col_dir

        while curr_row >= 0 and curr_row < rows \
          and curr_col >= 0 and curr_col < cols:
          if grid[curr_row][curr_col] == "#":
            occupied_seats += 1
            break
          elif grid[curr_row][curr_col] == "L":
            break

          curr_row += row_dir
          curr_col += col_dir

  return occupied_seats

def run_seating_simulation(abandon_threshold, count_func):
  seating_changed = True
  previous_seating = seating_grid
  while seating_changed:
    new_seating = deepcopy(previous_seating)
    seating_changed = False

    for row in range(rows):
      for col in range(cols):
        occupied_seats = count_func(previous_seating, row, col)
        if occupied_seats == 0 and new_seating[row][col] == "L":
          new_seating[row][col] = "#"
          seating_changed = True
        elif occupied_seats >= abandon_threshold and new_seating[row][col] == "#":
          new_seating[row][col] = "L"
          seating_changed = True

    previous_seating = new_seating

  return sum(sum(1 for node in row if node == "#") for row in new_seating)

def part1():
  return run_seating_simulation(4, count_occupied_seats)

def part2():
  return run_seating_simulation(5, count_occupied_seats_direction)

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())