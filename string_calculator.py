from functools import reduce 

def add(numbers: str) -> str:
    if (numbers == ""):
        return "0"

    return str(
        reduce(
            lambda a, b: int(a) + int(b),
            numbers.split(",")
        )
    )
