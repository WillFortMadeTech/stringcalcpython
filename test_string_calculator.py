from string_calculator import add
import pytest


def test_add_with_empty_string_returns_zero():
    assert add("") == "0"

@pytest.mark.parametrize("input_str,expected",
    [
        ["1", "1"],
        ["2", "2"],
        ["2,5", "7"],
        ["2.2,5.2", "7.4"],
        ["1.1,2.2", "3.3"],
        ["2.3,5.4", "7.7"]
    ]
)
def test_can_add_comma_separated_numbers(input_str, expected):
    assert add(input_str) == expected

@pytest.mark.parametrize("input_str,expected",
    [
        ["4\n5","9"],
        ["4\n5,6","15"]
    ]
)
def test_can_add_newline_as_a_separator(input_str, expected):
    assert add(input_str) == expected

@pytest.mark.parametrize("input_str,expected",
    [
        ["175.2,\n35","Number expected but '\n' found at position 6."]
    ]
)
def test_with_adjacent_separators(input_str, expected):
    assert add(input_str) == expected
