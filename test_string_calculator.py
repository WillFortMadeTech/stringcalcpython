from string_calculator import add


def test_add_with_empty_string_returns_zero():
    assert add("") is "0"

def test_add_with_1_returns_1():
    assert add("1") is "1"

def test_add_with_2_returns_2():
    assert add("2") is "2"
