with open("2021/Day 04/input.txt", "r") as f:
    lines = f.readlines()

calls = lines[0].replace("\n", "").split(",")
lines.pop(0)

board, boards = [], []
for line in lines:
    if line.strip() == "":
        if board:
            boards.append(board)
            board = []
    else:
        board.append(line.split())
boards.append(board)


def process_row(board, drawn):
    for row in board:
        if all(num in drawn for num in row):
            return True

    return False


def has_won(board, drawn, won):
    for x in range(len(board[0])):
        if all(line[x] in drawn for line in board):
            return True

    return won


# Part 1
def solve_part_1(calls, boards):
    for i in range(5, len(calls) + 1):
        drawn = set(calls[:i])

        for board in boards:
            won = has_won(board, drawn, process_row(board, drawn))

            if won:
                nonwon = sum(
                    [int(num) for line in board for num in line if num not in drawn]
                )

                return nonwon * int(calls[i - 1])


# Part 2
def solve_part_2(calls, boards):
    has_won_list = set()
    last_won = -1
    for i in range(5, len(calls) + 1):
        drawn = set(calls[:i])

        for j in range(len(boards)):
            if j in has_won_list:
                continue

            won = has_won(boards[j], drawn, process_row(boards[j], drawn))

            if won:
                has_won_list.add(j)
                last_won = j

        if len(has_won_list) == len(boards):
            nonwon = sum(
                [
                    int(num)
                    for line in boards[last_won]
                    for num in line
                    if num not in drawn
                ]
            )

            return nonwon * int(calls[i - 1])


print(solve_part_1(calls=calls, boards=boards))
print(solve_part_2(calls=calls, boards=boards))
