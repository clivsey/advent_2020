import re

rules = dict()
my_ticket = None
nearby_tickets = list()
parse_step = 0
rule_regex = re.compile("^([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$")

with open("day16_input.txt", "r") as puzzle_input:
  for line in puzzle_input:
    line = line.rstrip()  
    if parse_step == 0:
      rule_match = rule_regex.match(line)

      if rule_match:
        rules[rule_match.group(1)] = (int(rule_match.group(2)), int(rule_match.group(3)), int(rule_match.group(4)), int(rule_match.group(5)))
      elif line == "your ticket:":
        parse_step += 1
    elif parse_step == 1:
      if my_ticket == None:
        my_ticket = [int(num) for num in line.split(",")]
      # Wait until nearby_tickets: to advance, so we can discard other data
      elif line == "nearby tickets:":
        parse_step += 1
    elif parse_step == 2:
      nearby_tickets.append([int(num) for num in line.split(",")])

def part1():
  invalid_tickets = list()
  error_rate = 0
  for nearby_ticket in nearby_tickets:
    for num in nearby_ticket:
      for rule in rules.values():
        if num >= rule[0] and num <= rule[1]:
          break
        if num >= rule[2] and num <= rule[3]:
          break
      else:
        error_rate += num
        invalid_tickets.append(nearby_ticket)

  # For part 2, go ahead and remove invalid tickets from the source data
  for invalid_ticket in invalid_tickets:
    nearby_tickets.remove(invalid_ticket)

  return error_rate

def part2():
  total_fields = len(my_ticket)

  # Count how many valid fields are valid for which rule by index
  field_index = dict()

  while len(field_index) < total_fields:
    # Build a list of remaining eligible options for fields based on rules
    valid_rules_by_index = { index:{rule_name for rule_name in rules if rule_name not in field_index} \
      for index in range(total_fields) if index not in field_index.values() }

    for index in valid_rules_by_index.keys():
      for rule_name, rule in rules.items():
        if rule_name in field_index:
          continue

        for nearby_ticket in nearby_tickets:
          num = nearby_ticket[index]
          valid = (num >= rule[0] and num <= rule[1]) or (num >= rule[2] and num <= rule[3])
          if not valid:
            valid_rules_by_index[index].remove(rule_name)
            break

    # Update field mapping for anything that was successfully narrowed down
    for index, valid_rules in valid_rules_by_index.items():
      if len(valid_rules) == 1:
        field_index[next(iter(valid_rules))] = index

  dep_product = 1
  for field_name, i in field_index.items():
    if field_name.startswith("departure"):
      dep_product *= my_ticket[i]

  return dep_product

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())