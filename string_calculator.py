def add(numbers: str) -> str:
    if (numbers == ""):
        return "0"

    splitText = numbers.split(",")
    addition = 0
    for value in splitText:
        addition += int(value)
    return str(addition)

