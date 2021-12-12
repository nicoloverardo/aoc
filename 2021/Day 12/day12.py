from collections import defaultdict


def get_edges(lines):
    edges = defaultdict(list)
    for line in lines:
        x, y = line.split("-")

        edges[x].append(y)
        edges[y].append(x)

    return edges


def n_paths(lines, part2=False):
    edges = get_edges(lines)

    paths = set()
    p_list = [["start", a] for a in edges["start"]]

    while p_list:
        e = p_list.pop()
        nxt_nodes = [e + [a] for a in edges[e[-1]]]

        for node in nxt_nodes:
            if node[-1] == "end":
                if part2:
                    paths.add(tuple(node[1:]))
                else:
                    paths.add(tuple(node))
            elif part2 and node[-1] == "start":
                pass
            elif node[-1].isupper():
                p_list.append(node)
            elif node.count(node[-1]) == 1:
                p_list.append(node)
            elif part2 and (node.count(node[-1]) == 2 and node[0]):
                p_list.append([False] + node[1:])

    return len(paths)


with open("2021/Day 12/test_input.txt", "r") as f:
    test_lines = [line.replace("\n", "").strip() for line in f.readlines()]

with open("2021/Day 12/input.txt", "r") as f:
    input_lines = [line.replace("\n", "").strip() for line in f.readlines()]


assert n_paths(test_lines) == 10
print(n_paths(input_lines))

assert n_paths(test_lines, part2=True) == 36
print(n_paths(input_lines, part2=True))
