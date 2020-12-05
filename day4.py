import re

req_fields = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }
needed_fields = len(req_fields)
data_regex = re.compile("([a-z]{3}:[0-9a-z#]+)")

def part1():
  valid = 0

  with open("day4_input.txt", "r") as puzzle_input:
    req_match = 0
    for line in puzzle_input:
      match = data_regex.findall(line)

      # Empty match is empty line, which separates the entries
      if len(match) == 0:
        if req_match >= needed_fields:
          valid += 1

        req_match = 0
      else:
        # We only care about the field existing, not the actual data
        for i in range(len(match)):
          field = match[i][0:3]

          if field in req_fields:
            req_match += 1

    # Add the last one if valid
    if req_match >= needed_fields:
      valid += 1

  return valid

validators = {
  "byr": re.compile("^(19[2-9][0-9]|200[0-2])$"),
  "iyr": re.compile("^(201[0-9]|2020)$"),
  "eyr": re.compile("^(202[0-9]|2030)$"),
  "hgt": re.compile("^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$"),
  "hcl": re.compile("^#([0-9a-f]{6})$"),
  "ecl": re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$"),
  "pid": re.compile("^[0-9]{9}$"),
  "cid": re.compile(".*")
}

def part2():
  valid = 0

  with open("day4_input.txt", "r") as puzzle_input:
    req_match = 0
    for line in puzzle_input:
      match = data_regex.findall(line)

      # Empty match is empty line, which separates the entries
      if len(match) == 0:
        if req_match >= needed_fields:
          valid += 1

        req_match = 0
      else:
        for i in range(len(match)):
          field, value = match[i].split(":")

          # Validate the value, still have to check if required field due to not wanting cid to count
          if validators[field].match(value) and field in req_fields:
            req_match += 1

    # Add the last one if valid
    if req_match >= needed_fields:
      valid += 1

  return valid

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())