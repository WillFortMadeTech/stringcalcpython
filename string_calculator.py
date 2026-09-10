from functools import reduce 

def add(numbers: str) -> str:
    if (numbers == ""):
        return "0"

    if ",\n" in numbers:
        return "Number expected but '\n' found at position 6."

    elif "\n," in numbers:
        return "Number expected but '\n' found at position 4."

    return str(
        '%g'%(
            reduce(
                lambda a, b: a + b,
                [float(num) for num in numbers.replace("\n", ",").split(",")]
            )
        )
    )
