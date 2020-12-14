import re

input_regex = re.compile("^(mask|mem)\[*([0-9]*)\]* = ([X0-9]+)$")

with open("day14_input.txt", "r") as puzzle_input:
  instructions = [(match.group(1), int(match.group(2)) if match.group(1) == "mem" else None, \
    int(match.group(3)) if match.group(1) == "mem" else match.group(3)) \
    for line in puzzle_input for match in [input_regex.match(line.rstrip())] if match]

NUM_BITS = 36

def part1():
  mem_values = dict()

  for instruction in instructions:
    if instruction[0] == "mask":
      mask = instruction[2]
    else:
      # Get binary reprenstation of num
      mem_address = instruction[1]
      num_str = bin(instruction[2])[2:]
      pad_amount = NUM_BITS - len(num_str)

      # Convert to list to make the chars mutable
      num_str = list("0" * pad_amount + num_str)

      # Flip any bits from mask
      for i in range(NUM_BITS):
        if mask[i] != "X" and mask[i] != num_str[i]:
          num_str[i] = mask[i]

      mem_values[mem_address] = int("".join(num_str), 2)

  sum = 0
  for value in mem_values.values():
    sum += value

  return sum

def part2():
  mem_values = dict()

  for instruction in instructions:
    if instruction[0] == "mask":
      mask = instruction[2]
    else:
      # Turn into bin/list to make char mutable
      mem_address = list(format(instruction[1], "036b"))
      floating_bits = 0

      # Flip any bits from mask
      for i in range(NUM_BITS):
        if mask[i] == "X":
          floating_bits += 1
          mem_address[i] = "{}"
        elif mask[i] != "0":
          mem_address[i] = mask[i]

      # Flatten final representation
      mem_address = "".join(mem_address)

      if floating_bits > 0:
        # It just so happens that to get all the proper permutations, it's just 2 ^ N combinations and
        # the binary representation of numbers leading up to 2 ^ N
        bin_format = "0{}b".format(floating_bits)
        for i in range(2 ** floating_bits):
          replace_bits = format(i, bin_format)
          final_address = mem_address.format(*replace_bits)
          mem_values[int(final_address, 2)] = instruction[2]
      else:
        mem_values[int(mem_address, 2)] = instruction[2]

  sum = 0
  for value in mem_values.values():
    sum += value

  return sum

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())