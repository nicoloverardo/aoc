"""Day 1"""

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
        The calories of each elf, including blanks.
    """

    with open(Path(f_path), encoding="utf8") as f_stream:
        return [item.replace("\n", "").strip() for item in f_stream.readlines()]


def elves_sorter(data: List[str]) -> List[int]:
    """Reads the input and gets the total calories for
    each elf sorted in descending order.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    List[int]
        The calories of each elf.
    """

    elves = []
    elf = 0

    for item in data:
        if item != "":
            elf += int(item)
            continue

        elves.append(elf)
        elf = 0

    elves.append(elf)

    return sorted(elves, reverse=True)


def solution_1(**kwargs) -> int:
    """Solution part 1 for day 1.

    Parameters
    ----------
    **kwargs
        Arguments passed to `elves_sorter()`.

    Returns
    -------
    int
        The Elf with max calories.
    """

    return max(elves_sorter(**kwargs))


def solution_2(**kwargs) -> int:
    """Solution part 2 for day 1.

    Parameters
    ----------
    **kwargs
        Arguments passed to `elves_sorter()`.

    Returns
    -------
    int
        The sum of the top three Elves carrying
        the most Calories.
    """

    return sum(elves_sorter(**kwargs)[:3])


if __name__ == "__main__":
    input_data = read_data()
    test_input_data = read_data("test_input.txt")

    print("Testing part 1:", solution_1(data=test_input_data), "- Expected: 24000")
    print("Testing part 2:", solution_2(data=test_input_data), "- Expected: 45000")
    print("Solution part 1:", solution_1(data=input_data))
    print("Solution part 2:", solution_2(data=input_data))
