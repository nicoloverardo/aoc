"""Day 5"""

from pathlib import Path
from typing import Union, List, Tuple


def read_data(f_path: Union[str, Path] = Path("input.txt")) -> List[str]:
    """Reads the input to list.

    Parameters
    ----------
    f_path : str or Path, optional
        The input txt file, by default "input.txt"

    Returns
    -------
    List[str]
        The list of pairs of elves.
    """

    with open(Path(f_path), encoding="utf8") as f_stream:
        return [item.replace("\n", "") for item in f_stream.readlines()]


def solver(data: List[str], reverse: bool = False) -> str:
    """Moves the boxes from the stacks.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    str
        The top stacks.
    """

    index_split = [i for i in range(0, len(data)) if data[i] == ""]
    input_stacks = data[: index_split[0]]
    moves_list = __parse_moves(data[index_split[0] + 1 :])
    n_cols = int(input_stacks[-1].strip()[-1])
    _ = input_stacks.pop()

    res = {}
    j = 1
    for i in range(1, n_cols + 1):
        res[i] = [item[j] for item in input_stacks if item[j] != " "]
        j += 4

    res = {key: list(reversed(value)) for key, value in res.items()}

    for item in moves_list:
        n_moves, stack_source, stack_dest = item

        tmp_dest = res[stack_dest].copy()
        to_add_list = res[stack_source][-n_moves:]

        tmp_dest.extend(list(reversed(to_add_list)) if reverse else to_add_list)

        res[stack_dest] = tmp_dest
        res[stack_source] = res[stack_source][:-n_moves]

    return "".join([item[-1] for item in res.values()])


def __parse_moves(data: List[str]) -> List[Tuple[int, int, int]]:
    moves_parsed = [
        tuple(
            item.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        )
        for item in data
    ]

    return [
        (int(n_moves), int(stack_source), int(stack_dest))
        for n_moves, stack_source, stack_dest in moves_parsed
    ]


def solution_1(data: List[str]) -> str:
    """Solution part 1 for day 5.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    str
        The top boxes.
    """
    return solver(data, reverse=True)


def solution_2(data: List[str]) -> str:
    """Solution part 2 for day 5.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    str
        The top boxes.
    """
    return solver(data, reverse=False)


if __name__ == "__main__":
    input_data = read_data()
    test_input_data = read_data("test_input.txt")

    print("Testing part 1:", solution_1(data=test_input_data), "- Expected: CMZ")
    print("Testing part 2:", solution_2(data=test_input_data), "- Expected: MCD")
    print("Solution part 1:", solution_1(data=input_data))
    print("Solution part 2:", solution_2(data=input_data))
