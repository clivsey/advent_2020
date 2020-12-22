with open("day18_input.txt", "r") as puzzle_input:
  all_lines = [line.rstrip() for line in puzzle_input]

op_func = {
  "+": (lambda x, y: x + y),
  "*": (lambda x, y: x * y),
}

def parse_line(line, op_precedence):
  output = list()
  operators = list()

  for token in line:
    if token in op_precedence:
      while len(operators) > 0 and operators[-1] != "(" and op_precedence[operators[-1]] >= op_precedence[token]:
        output.append(operators.pop())
      operators.append(token)
    elif token == "(":
      operators.append(token)
    elif token == ")":
      while operators[-1] != "(":
        output.append(operators.pop())
      operators.pop()
    elif token != " ":
      output.append(int(token))

  while len(operators) > 0:
    output.append(operators.pop())

  return output

def parse_rpn(rpn):
  stack = list()
  for token in rpn:
    if token in op_func:
      stack.append(op_func[token](stack.pop(), stack.pop()))
    else:
      stack.append(token)
  return stack.pop()

def part1():
  sum = 0
  for line in all_lines:
    rpn = parse_line(line, { "+": 1, "*": 1 })
    sum += parse_rpn(rpn)

  return sum

def part2():
  sum = 0
  for line in all_lines:
    rpn = parse_line(line, { "+": 2, "*": 1 })
    sum += parse_rpn(rpn)

  return sum

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())