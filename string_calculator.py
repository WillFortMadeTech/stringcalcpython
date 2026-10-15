import re
from functools import reduce


def add(numbers: str) -> str:

    separators = [",", "\n"]

    if numbers == "":
        return "0"

    try:
        __validate_input(separators, numbers)

        numbers_array = re.split("|".join(map(re.escape, separators)), numbers)

        return str(
            "%g" % (reduce(lambda a, b: a + b, [float(num) for num in numbers_array]))
        )
    except ValueError as error:
        return str(error)


def __validate_input(separators, numbers):
    __last_character_of_input_must_not_be_separator(separators, numbers)
    __must_not_include_empty_number(separators, numbers)


def __last_character_of_input_must_not_be_separator(separators, numbers):
    if numbers[len(numbers) - 1] in separators:
        raise ValueError("Number expected but EOF found")


def __must_not_include_empty_number(separators, numbers):
    for position in range(1, len(numbers)):
        if numbers[position] in separators and numbers[position - 1] in separators:
            raise ValueError(
                f"Number expected but '{numbers[position]}' found at position {position}."
            )
