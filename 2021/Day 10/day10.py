from statistics import median

char_list_left = ["(", "[", "{", "<"]
char_list_right = [")", "]", "}", ">"]
char_scores_corrupt = [3, 57, 1197, 25137]

char_matches = dict(zip(char_list_right, char_list_left))
char_scores = dict(zip(char_list_right, char_scores_corrupt))

char_scores_incomplete = dict(zip(char_list_left, list(range(1, 5))))


def calc_corrupt_score(lines):
    score = 0
    pstack = []
    for line in lines:
        for c in line:
            if c in char_list_left:
                pstack.append(c)
            else:
                if c in char_list_right:
                    if pstack[-1] != char_matches[c]:
                        score += char_scores[c]
                    pstack.pop()

    return score


def calc_incompl_score(lines):
    scores = []
    for line in lines:
        pstack = []
        corrupt = False
        for c in line:
            if c in char_list_left:
                pstack.append(c)
            else:
                if c in char_list_right:
                    if not pstack or pstack.pop() != char_matches[c]:
                        corrupt = True
                        break

        if corrupt:
            continue

        score = 0
        for c in pstack[::-1]:
            score *= 5
            score += char_scores_incomplete[c]

        scores.append(score)

    return median(scores)


with open("2021/Day 10/test_input.txt", "r") as f:
    test_lines = [line.replace("\n", "").strip() for line in f.readlines()]

with open("2021/Day 10/input.txt", "r") as f:
    input_lines = [line.replace("\n", "").strip() for line in f.readlines()]

assert calc_corrupt_score(test_lines) == 26397

print(str(calc_corrupt_score(input_lines)))

assert calc_incompl_score(test_lines) == 288957

print(str(calc_incompl_score(input_lines)))
