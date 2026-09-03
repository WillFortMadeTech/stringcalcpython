from string_calculator import add


def test_add_with_empty_string_returns_zero():
    assert add("") == "0"

def test_add_with_1_returns_1():
    assert add("1") == "1"

def test_add_with_2_returns_2():
    assert add("2") == "2"

def test_add_with_2_and_5_returns_7():
    assert add("2,5") == "7"

def test_add_with_2point4_and_5point3_returns_7point7():
    assert add("2.4,5.3") == "7.7"
