from statistics import median

with open("2021/Day 07/input.txt", "r") as f:
    vals = list(map(int, f.read().strip().split(",")))

# Part one
mdn = median(vals)
dists = [abs(mdn - x) for x in vals]
print(str(int(sum(dists))))

# Part 2
fuel = lambda d: d * (d + 1) // 2

outcomes = []
for y in range(min(vals), max(vals) + 1):
    outcomes.append(sum([fuel(max(x, y) - min(x, y)) for x in vals]))

print(str(min(outcomes)))
