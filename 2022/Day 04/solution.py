"""Day 4"""

from pathlib import Path
from typing import Union, List, Tuple, Callable


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
        return [item.replace("\n", "").strip() for item in f_stream.readlines()]


def solver(data: List[str], func: Callable) -> int:
    """Find the overlapping sections

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    int
        The total overlaps
    """

    splitted = [line.split(",") for line in data]
    couples = [
        (section_to_list(first), section_to_list(second)) for first, second in splitted
    ]

    return sum(func(item) for item in couples)


def section_to_list(section: str) -> List[int]:
    """Converts a string separated by dash and generates
    the range of numbers with start and end as the splitted
    items.

    Parameters
    ----------
    section : str
        The source data

    Returns
    -------
    List[int]
        The list of numbers.
    """

    start, end = section.split("-")
    return list(range(int(start), int(end) + 1))


def full_coverage_check(sections: Tuple[List[int]]) -> int:
    """Checks for full overlapping numbers.

    Parameters
    ----------
    sections : Tuple[List[int]]
        The tuple of two elves.

    Returns
    -------
    int
        The sum of full overlapping sections.
    """

    first, second = sections

    if len(set(first) - set(second)) == 0 or len(set(second) - set(first)) == 0:
        return 1

    return 0


def any_duplicate_check(sections: Tuple[List[int]]) -> int:
    """Checks if there is any overlapping item.

    Parameters
    ----------
    sections : Tuple[List[int]]
        The tuple of two elves.

    Returns
    -------
    int
        The sum of overlapping sections.
    """

    first, second = sections

    if (
        len(set(first).intersection(set(second))) > 0
        or len(set(second).intersection(set(first))) > 0
    ):
        return 1

    return 0


def solution_1(data: List[str]) -> int:
    """Solution part 1 for day 4.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    int
        The full ovelapping.
    """

    return solver(data, full_coverage_check)


def solution_2(data: List[str]) -> int:
    """Solution part 2 for day 4.

    Parameters
    ----------
    data : List[str]
        The loaded input.

    Returns
    -------
    int
        Any ovelapping section.
    """

    return solver(data, any_duplicate_check)


if __name__ == "__main__":
    input_data = read_data()
    test_input_data = read_data("test_input.txt")

    print("Testing part 1:", solution_1(data=test_input_data), "- Expected: 2")
    print("Testing part 2:", solution_2(data=test_input_data), "- Expected: 4")
    print("Solution part 1:", solution_1(data=input_data))
    print("Solution part 2:", solution_2(data=input_data))
