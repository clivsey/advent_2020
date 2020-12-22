from copy import deepcopy

# Mostly using dict so we can use x,y,z as keys, rather than building an infinite grid
matrix = dict()

with open("day17_input.txt", "r") as puzzle_input:
  grid = [[char for char in line.rstrip()] for line in puzzle_input]

  for y, row in enumerate(grid):
    for x, node in enumerate(row):
      matrix[(x, y, 0, 0)] = node == "#"

def count_active_p1(base_matrix, x, y, z, w):
  active_near = 0
  for xx in range(x - 1, x + 2):
    for yy in range(y - 1, y + 2):
      for zz in range(z - 1, z + 2):
        if xx != x or yy != y or zz != z:
          if base_matrix.get((xx, yy, zz, 0), False):
            active_near += 1

  return active_near

def count_active_p2(base_matrix, x, y, z, w):
  active_near = 0
  for xx in range(x - 1, x + 2):
    for yy in range(y - 1, y + 2):
      for zz in range(z - 1, z + 2):
        for ww in range(w - 1, w + 2):
          if xx != x or yy != y or zz != z or ww != w:
            if base_matrix.get((xx, yy, zz, ww), False):
              active_near += 1

  return active_near

def simulate_node(base_matrix, active_matrix, count_active, x, y, z, w):
  node_changed = False
  node_tuple = (x, y, z, w)
  node_active = base_matrix.get(node_tuple, False)
  active_near = count_active(base_matrix, x, y, z, w)

  if not node_active and active_near == 3:
    active_matrix[node_tuple] = True
    node_changed = True
  elif node_active and (active_near != 2 and active_near != 3):
    active_matrix[node_tuple] = False
    node_changed = True

  return node_changed

def part1():
  part1_matrix = deepcopy(matrix)
  prev_matrix = matrix
  max_offset = 15

  for _ in range(6):
    for x in range(-max_offset, max_offset + 1):
      for y in range(-max_offset, max_offset + 1):
        for z in range(-max_offset, max_offset + 1):
          simulate_node(prev_matrix, part1_matrix, count_active_p1, x, y, z, 0)

    prev_matrix = part1_matrix
    part1_matrix = deepcopy(prev_matrix)

  return sum(1 for node in part1_matrix.values() if node)

def part2():
  part2_matrix = deepcopy(matrix)
  prev_matrix = matrix
  max_offset = 15

  for _ in range(6):
    for x in range(-max_offset, max_offset + 1):
      for y in range(-max_offset, max_offset + 1):
        for z in range(-max_offset, max_offset + 1):
          for w in range(-max_offset, max_offset + 1):
            simulate_node(prev_matrix, part2_matrix, count_active_p2, x, y, z, w)

    prev_matrix = part2_matrix
    part2_matrix = deepcopy(prev_matrix)

  return sum(1 for node in part2_matrix.values() if node)

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())