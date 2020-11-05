# List Comprehensions
# https://www.hackerrank.com/challenges/list-comprehensions/problem

max_x = 1
max_y = 1
max_z = 2
n = 3

combinations = [[x, y, z] for x in range(max_x+1) for y in range(max_y+1) for z in range(max_z + 1) if not x + y + z == n]
print(combinations)


# without comprehension:
all_combinations = []

for x in range(max_x + 1):
    for y in range(max_y + 1):
        for z in range(max_z + 1):
            if not x + y + z == n:
                all_combinations.append([x, y, z])

print(all_combinations)