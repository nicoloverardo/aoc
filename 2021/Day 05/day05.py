with open("2021/Day 05/input.txt", "r") as f:
    lines = [
        tuple(map(int, line.replace("\n", "").replace(" -> ", ",").split(",")))
        for line in f.readlines()
    ]

sign = lambda n: 1 if n > 0 else -1 if n < 0 else 0

res1, res2 = {}, {}
for a, b, c, d in lines:
    for i in range(max(abs(c - a), abs(d - b)) + 1):
        x = a + i * sign(c - a)
        y = b + i * sign(d - b)

        if (x, y) not in res2:
            res2[(x, y)] = 1
        else:
            res2[(x, y)] += 1
        if abs(c - a) == 0 or abs(d - b) == 0:
            if (x, y) not in res1:
                res1[(x, y)] = 1
            else:
                res1[(x, y)] += 1


print(sum(x >= 2 for x in res1.values()))
print(sum(x >= 2 for x in res2.values()))
