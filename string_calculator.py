from functools import reduce 

def add(numbers: str) -> str:
    if (numbers == ""):
        return "0"

    return str(
        '%g'%(
            reduce(
                lambda a, b: a + b,
                [float(num) for num in numbers.split(",")]
            )
        )
    )
