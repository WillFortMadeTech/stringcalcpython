from string_calculator import add


def test_add_with_empty_string_returns_zero():
    result = add("")

    assert result is "0"

def test_add_with_1_returns_1():
    result = add("1")

    assert result is "1"

def test_add_with_2_returns_2():
    result = add("2")
    
    assert result is "2"
