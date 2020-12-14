import math
import re

line_regex = re.compile("([NESWLRF]{1})([0-9]{1,3})")

with open("day12_input.txt", "r") as puzzle_input:
  instructions = [(match.group(1), int(match.group(2))) for line in puzzle_input for match in [line_regex.match(line.rstrip())]]

dir_index = { "N": 0, "E": 1, "S": 2, "W": 3 }
dir_velocity = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

def part1():
  current_dir = 1
  x = 0
  y = 0

  for instruction in instructions:
    move_dir = instruction[0]
    move_amount = instruction[1]

    if move_dir == "L" or move_dir == "R":
      # Rotate based on index
      rotations = move_amount // 90
      current_dir += -rotations if move_dir == "L" else rotations

      # Wrap around if we rotated past
      while current_dir < 0:
        current_dir += 4
      while current_dir >= 4:
        current_dir -= 4
    else:
      if move_dir == "F":
        vel_dir = current_dir
      else:
        vel_dir = dir_index[move_dir]

      x += dir_velocity[vel_dir][0] * move_amount
      y += dir_velocity[vel_dir][1] * move_amount

  return abs(x) + abs(y)

def part2():
  waypoint_x, waypoint_y = 10, 1
  ship_x, ship_y = 0, 0

  for instruction in instructions:
    move_dir = instruction[0]
    move_amount = instruction[1]

    if move_dir == "L" or move_dir == "R":
      # Flip move_amount if R to rotate clockwise
      if move_dir == "R":
        move_amount = -move_amount
      
      # Convert to radians
      move_amount = math.radians(move_amount)
      
      # Rotate first, don't want to change X before calculating Y
      rotate_x = waypoint_x * math.cos(move_amount) - waypoint_y * math.sin(move_amount)
      rotate_y = waypoint_y * math.cos(move_amount) + waypoint_x * math.sin(move_amount)

      # Since we're dealing with radians (floating point), round the result
      waypoint_x = round(rotate_x)
      waypoint_y = round(rotate_y)
    else:
      if move_dir == "F":
        ship_x += waypoint_x * move_amount
        ship_y += waypoint_y * move_amount
      else:
        vel_dir = dir_index[move_dir]
        waypoint_x += dir_velocity[vel_dir][0] * move_amount
        waypoint_y += dir_velocity[vel_dir][1] * move_amount

  return abs(ship_x) + abs(ship_y)

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())