import re
from functools import reduce



def add(numbers: str) -> str:

    separators = [",", "\n"]

    if numbers == "":
        return "0"
    
    errors = __validate_input(separators, numbers)
    if errors:
        return errors

    numbers_array = re.split("|".join(map(re.escape, separators)), numbers)

    return str(
        '%g'%(
            reduce(
                lambda a, b: a + b,
                [float(num) for num in numbers_array]
            )
        )
    )

def __validate_input(separators, numbers):
    for position in range(1, len(numbers)):
        if numbers[position] in separators and numbers[position - 1] in separators:
            return f"Number expected but '{numbers[position]}' found at position {position}."
    return None


