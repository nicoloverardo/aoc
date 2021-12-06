from collections import Counter, defaultdict

with open("2021/Day 06/input.txt", "r") as f:
    line = list(map(int, f.read().split(",")))

cnt = Counter(line)


def get_population(cnt: Counter, days: int):
    for _ in range(days):
        d = defaultdict(int)

        for v in cnt:
            if v == 0:
                d[6] += cnt[0]
                d[8] += cnt[0]
            else:
                d[v - 1] += cnt[v]

        cnt = d

    return sum(cnt.values())


print(get_population(days=80, cnt=cnt))
print(get_population(days=256, cnt=cnt))
