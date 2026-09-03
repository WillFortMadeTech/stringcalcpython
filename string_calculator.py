from functools import reduce 

def add(numbers: str) -> str:
    if (numbers == ""):
        return "0"

    splitText = numbers.split(",")
    ans = reduce(lambda a, b: int(a) + int(b), splitText)
    return str(ans)

