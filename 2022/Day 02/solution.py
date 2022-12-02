"""Day 2"""

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
        The rounds
    """

    with open(Path(f_path), encoding="utf8") as f_stream:
        return [i.replace(" ", "") for i in f_stream.read().strip().split("\n")]


def solution_1(data: List[str]) -> int:
    """Solution part 1 for day 2.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    int
        The total score.
    """

    all_outcomes = {
        "AX": 4,
        "AY": 8,
        "AZ": 3,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 7,
        "CY": 2,
        "CZ": 6,
    }

    return sum(all_outcomes[round] for round in data)


def solution_2(data: List[str]) -> int:
    """Solution part 2 for day 2.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    int
        The total score
    """

    all_outcomes = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7,
    }

    return sum(all_outcomes[round] for round in data)


if __name__ == "__main__":
    input_data = read_data()
    test_input_data = read_data("test_input.txt")

    print("Testing part 1:", solution_1(data=test_input_data), "- Expected: 15")
    print("Testing part 2:", solution_2(data=test_input_data), "- Expected: 12")
    print("Solution part 1:", solution_1(data=input_data))
    print("Solution part 2:", solution_2(data=input_data))
