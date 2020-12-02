import re

with open("day2_input.txt", "r") as puzzle_input:
  passwords = [line for line in puzzle_input]

password_regex = re.compile("([0-9]+)-([0-9]+) ([A-Za-z]): ([A-Za-z]+)")
def part1():
  valid = 0

  for password in passwords:
    match = password_regex.match(password)
    min_count = int(match.group(1))
    max_count = int(match.group(2))
    match_char = match.group(3)
    password = match.group(4)
    
    match_count = password.count(match_char)
    if match_count >= min_count and match_count <= max_count:
      valid += 1

  return valid

def part2():
  valid = 0

  for password in passwords:
    match = password_regex.match(password)
    first_index = int(match.group(1)) - 1
    second_index = int(match.group(2)) - 1
    match_char = match.group(3)
    password = match.group(4)
    
    if ((password[first_index] == match_char or password[second_index] == match_char)
        and password[first_index] != password[second_index]):
      valid += 1

  return valid

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())