from functools import reduce 



def add(numbers: str) -> str:
    
    errors = __validate_input(numbers)
    if(errors):
        return errors

    if (numbers == ""):
        return "0"

    return str(
        '%g'%(
            reduce(
                lambda a, b: a + b,
                [float(num) for num in numbers.replace("\n", ",").split(",")]
            )
        )
    )

def __validate_input(numbers):
    if ",\n" in numbers:
        return "Number expected but '\n' found at position 6."

    elif "\n," in numbers:
        return "Number expected but '\n' found at position 4."


