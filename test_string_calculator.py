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
        ["4\n5","9"]
    ]
)
def test_can_add_newline_as_a_separator(input_str, expected):
    assert add(input_str) == expected
