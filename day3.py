import re

with open("day3_input.txt", "r") as puzzle_input:
  grid = [char for line in puzzle_input for char in line.rstrip()]

cols = 31
rows = len(grid) // cols

def get_trees_from_slope(vel_x, vel_y):
  curr_x = 0
  curr_y = 0
  trees = 0

  # While we will always hit the break inside first, this still feels better than while True
  while curr_y < rows:
    curr_x += vel_x
    curr_y += vel_y

    while curr_x >= cols:
      curr_x -= cols
    
    # Break out before accessing array to prevent out of bounds
    if curr_y >= rows:
      break

    if grid[curr_y * cols + curr_x] == "#":
      trees += 1

  return trees

def part1():
  return get_trees_from_slope(3, 1)

def part2():
  return get_trees_from_slope(1, 1) * \
         get_trees_from_slope(3, 1) * \
         get_trees_from_slope(5, 1) * \
         get_trees_from_slope(7, 1) * \
         get_trees_from_slope(1, 2)

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())