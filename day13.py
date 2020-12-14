import math

with open("day13_input.txt", "r") as puzzle_input:
  earliest_departure = int(puzzle_input.readline())
  bus_schedule = puzzle_input.readline().split(",")

def part1():
  valid_bus_ids = [int(bus_id) for bus_id in bus_schedule if bus_id != "x"]
  best_bus = None
  best_departure_time = None

  # Find the bus with the closest departure time compared to earliest_depature
  for bus_id in valid_bus_ids:
    wait_time = bus_id - earliest_departure % bus_id
    bus_departure_time = earliest_departure + wait_time

    if best_bus == None or best_departure_time > bus_departure_time:
      best_bus = bus_id
      best_departure_time = bus_departure_time

  return best_bus * (best_departure_time - earliest_departure)

def part2():
  bus_ids = [(int(bus_id), i) for i, bus_id in enumerate(bus_schedule) if bus_id != "x"]
  timestamp, step = 0, 1
  
  for bus_id, bus_index in bus_ids:
    # Find the first product that has zero remainder based timestamp being offset by bus_index
    while (timestamp + bus_index) % bus_id != 0:
      timestamp += step
    
    # Because we are multiplying by bus_id, this ensures all previous bus_ids can factor into the new step
    step *= bus_id
      
  return timestamp

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())