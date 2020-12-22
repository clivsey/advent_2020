import re

rule_regex = re.compile("^([0-9]+): ([0-9 ab\|\"]+)$")

rules = dict()
messages = list()

with open("day19_input.txt", "r") as puzzle_input:
  for line in puzzle_input:
    line = line.rstrip()
    rule_match = rule_regex.match(line)
    if rule_match:
      # Parse rule_id:defintition from regex
      rule_id = int(rule_match.group(1))
      rule_definition = rule_match.group(2)

      # Keep track of rule parts by list
      rules[rule_id] = list()

      if rule_definition.startswith("\""):
        rules[rule_id].append(rule_definition[1])
      else:
        rule_parts = rule_definition.split(" | ")
        for rule_part in rule_parts:
          rules[rule_id].append([int(inner_rule_id) for inner_rule_id in rule_part.split(" ")])
    elif line != "":
      messages.append(line)

def get_rule_regex(rule_id, depth, max_depth):
  regex_string = "("

  # Keeping track of depth let's us avoid any special cases or branches for part 2
  if depth <= max_depth:
    for i, rule in enumerate(rules[rule_id]):
      if i > 0:
        regex_string += "|"

      if isinstance(rule, list):
        for inner_rule in rule:
          if inner_rule in rules:
            regex_string += get_rule_regex(inner_rule, depth + 1, max_depth)
      else:
        regex_string += rule
  
  regex_string += ")"

  return regex_string

def part1():
  rule_zero_regex = re.compile("^" + get_rule_regex(0, 0, 24) + "$")
  return sum(1 for message in messages if rule_zero_regex.match(message))

def part2():
  # Replace rules
  rules[8] = [[42], [42, 8]]
  rules[11] = [[42, 31], [42, 11, 31]]

  # Same as part 1
  rule_zero_regex = re.compile("^" + get_rule_regex(0, 0, 24) + "$")
  return sum(1 for message in messages if rule_zero_regex.match(message))

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())