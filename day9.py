from collections import deque
import sys

with open("day9_input.txt", "r") as puzzle_input:
  input_nums = [int(line.rstrip()) for line in puzzle_input]

def two_sum(nums, target):
  seen = set()
  for num in nums:
    diff = target - num
    if diff in seen:
      return True
    seen.add(num)

  return False

def part1():
  # deque to keep track of the most recent 25 nums
  preamble = deque()
  for i in range(25):
    preamble.append(input_nums[i])

  # All we need to do is go through each num and two_sum against prev 25
  for i in range(26, len(input_nums)):
    if not two_sum(preamble, input_nums[i]):
      return input_nums[i]

    preamble.popleft()
    preamble.append(input_nums[i])

  return 0
  
def part2():
  target = part1()
  
  left = 0
  right = 1
  current_sum = input_nums[left] + input_nums[right]
  max_idx = len(input_nums) - 1

  while right < max_idx:
    # Grow the range while smaller
    while right < max_idx and (current_sum < target or left == right - 1):
      right += 1
      current_sum += input_nums[right]

    # Shrink the range while bigger
    while left < right - 1 and current_sum > target:
      left += 1
      current_sum -= input_nums[left - 1]

    if current_sum == target:
      break

  # We could have attempted to track this above, but keeping it simple, due to sliding window
  smallest = sys.maxsize
  largest = 0
  for i in range(left, right + 1):
    if smallest > input_nums[i]:
      smallest = input_nums[i]
    if largest < input_nums[i]:
      largest = input_nums[i]

  return smallest + largest

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())