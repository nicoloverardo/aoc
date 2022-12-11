"""Day 07"""

from enum import Enum
from pathlib import Path
from typing import Union, List


def from_str(value, enum_obj):
    """Convert string to Enum."""
    value = value.lower()

    for element in enum_obj:
        if value == element.value:
            return element
    return None


class SpecialFolders(Enum):
    """Represents some special folders"""

    ROOT = "/"
    FOL_UP = ".."

    @staticmethod
    def from_str(value):
        return from_str(value, SpecialFolders)


class CliCommands(Enum):
    """Represents the possible Cli commands"""

    CD = "cd"
    LS = "ls"

    @staticmethod
    def from_str(value):
        return from_str(value, CliCommands)


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


def is_command(line: str) -> bool:
    """Indicates whether a string is a Cli command."""
    return line.startswith("$")


def is_file(line: str) -> bool:
    """Indicates whether a string is a file."""
    return line[0].isdigit()


def solver(data: List[str]) -> dict:
    """Solver for day 07"""

    dirs = {}
    current_dirs = []

    splitted = [line.split(" ") for line in data]
    for line in splitted:
        if is_file(line[0]):
            for d in current_dirs:
                dirs[d] += int(line[0])
            continue

        if is_command(line[0]) and CliCommands.from_str(line[1]) == CliCommands.CD:
            if SpecialFolders.from_str(line[2]) == SpecialFolders.FOL_UP:
                current_dirs.pop()
                continue

            if SpecialFolders.from_str(line[2]) == SpecialFolders.ROOT:
                current_dirs = ["//"]
                dirs["//"] = 0
                continue

            local_dir = "/".join(current_dirs) + "/" + line[2]
            current_dirs.append(local_dir)
            if not dirs.get(local_dir):
                dirs[local_dir] = 0

    return dirs


def solution_1(data: List[str]) -> int:
    """Solution part 1 day 7"""

    return sum(x for x in solver(data).values() if x <= 100000)


def solution_2(data: List[str]) -> int:
    """Solution part 2 day 7"""

    result = solver(data)
    space_needed = result["//"] - 40000000
    return min(x for x in result.values() if x > space_needed)


if __name__ == "__main__":
    input_data = read_data()
    test_input_data = read_data("test_input.txt")

    print("Testing part 1:", solution_1(data=test_input_data), "- Expected: CMZ")
    print("Testing part 2:", solution_2(data=test_input_data), "- Expected: MCD")
    print("Solution part 1:", solution_1(data=input_data))
    print("Solution part 2:", solution_2(data=input_data))
