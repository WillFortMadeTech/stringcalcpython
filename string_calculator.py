from functools import reduce 

def add(numbers: str) -> str:
    if (numbers == ""):
        return "0"

    return str(
        '%g'%(
            float(
                reduce(
                    lambda a, b: float(a) + float(b),
                    numbers.split(",")
                )
            )
        )
    )
