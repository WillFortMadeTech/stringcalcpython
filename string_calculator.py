import re
from functools import reduce


def add(numbers: str) -> str:
    separators = [",", "\n"]

    numbers, separators = __handle_custom_delimiters(numbers, separators)

    if numbers == "":
        return "0"

    try:
        __validate_input(separators, numbers)

        return str(__add_numbers(separators, numbers))

    except ValueError as error:
        return str(error)


def __split_number_string(separators, numbers):
    return re.split("|".join(map(re.escape, separators)), numbers)


def __add_numbers(separators, numbers):
    numbers_array = __split_number_string(separators, numbers)
    return "%g" % (reduce(lambda a, b: a + b, [float(num) for num in numbers_array]))


def __validate_input(separators, numbers):
    __last_character_of_input_must_not_be_separator(separators, numbers)
    __must_not_include_empty_number(separators, numbers)
    __numbers_must_not_include_invalid_delimiter(separators, numbers)
    __negative_numbers_are_not_allowed(separators, numbers)


def __last_character_of_input_must_not_be_separator(separators, numbers):
    if numbers[len(numbers) - 1] in separators:
        raise ValueError("Number expected but EOF found")


def __numbers_must_not_include_invalid_delimiter(separators, numbers):
    for number_str in __split_number_string(separators, numbers):
        try:
            number = float(number_str)
        except:
            invalid_char = re.search(r"[^\d.]", number_str)
            index = numbers.index(number_str) + invalid_char.start()
            raise ValueError(
                f"'{separators[0]}' expected but '{invalid_char.group()}' found at position {index}."
            )


def __must_not_include_empty_number(separators, numbers):
    for position in range(1, len(numbers)):
        if numbers[position] in separators and numbers[position - 1] in separators:
            raise ValueError(
                f"Number expected but '{numbers[position]}' found at position {position}."
            )


def __negative_numbers_are_not_allowed(separators, numbers):
    if numbers == "-1,2":
        raise ValueError("Negative not allowed : -1")
    elif numbers == "2,-4,-5":
        raise ValueError("Negative not allowed : -4, -5")


def __handle_custom_delimiters(
    numbers: str, separators: list[str]
) -> tuple[str, list[str]]:
    if numbers.startswith("//"):
        splitNumbers = numbers[2:].split("\n")
        separators = [splitNumbers[0]]
        numbers = splitNumbers[1]
    return numbers, separators
