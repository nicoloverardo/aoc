"""Day 3"""

import string
from pathlib import Path
from typing import Union, List


def read_data(f_path: Union[str, Path] = Path("input.txt")) -> List[str]:
    """Reads the input to list.

    Parameters
    ----------
    f_path : str or Path, optional
        The input txt file, by default "input.txt"

    Returns
    -------
    List[str]
        The list of rucksacks.
    """

    with open(Path(f_path), encoding="utf8") as f_stream:
        return [item.replace("\n", "").strip() for item in f_stream.readlines()]


def solver(data: List[str]) -> int:
    """Maps letters to their priorities.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    int
        The total priority.
    """

    values_map = dict(zip(string.ascii_letters, list(range(1, 53))))

    return sum(values_map[item] for item in data)


def solution_1(data: List[str]) -> int:
    """Solution part 1 for day 3.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    int
        The total priority.
    """

    splitted = [(item[: len(item) // 2], item[len(item) // 2 :]) for item in data]
    common = [list(set(first).intersection(second))[0] for first, second in splitted]

    return solver(common)


def solution_2(data: List[str]) -> int:
    """Solution part 2 for day 3.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    int
        The total priority.
    """

    data_by_three = list(zip(*(iter(data),) * 3))
    common = [
        list(set(first).intersection(second).intersection(third))[0]
        for first, second, third in data_by_three
    ]

    return solver(common)


if __name__ == "__main__":
    input_data = read_data()
    test_input_data = read_data("test_input.txt")

    print("Testing part 1:", solution_1(data=test_input_data), "- Expected: 157")
    print("Testing part 2:", solution_2(data=test_input_data), "- Expected: 70")
    print("Solution part 1:", solution_1(data=input_data))
    print("Solution part 2:", solution_2(data=input_data))
