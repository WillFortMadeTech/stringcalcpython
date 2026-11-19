from string_calculator import add
import pytest


def test_add_with_empty_string_returns_zero():
    assert add("") == "0"


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ["1", "1"],
        ["2", "2"],
        ["2,5", "7"],
        ["2.2,5.2", "7.4"],
        ["1.1,2.2", "3.3"],
        ["2.3,5.4", "7.7"],
    ],
)
def test_can_add_comma_separated_numbers(input_str, expected):
    assert add(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [["4\n5", "9"], ["4\n5,6", "15"]])
def test_can_add_newline_as_a_separator(input_str, expected):
    assert add(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ["175.2,\n35", "Number expected but '\n' found at position 6."],
        ["17\n,35", "Number expected but ',' found at position 3."],
        ["17,,35", "Number expected but ',' found at position 3."],
        ["17\n\n35", "Number expected but '\n' found at position 3."],
    ],
)
def test_with_adjacent_separators(input_str, expected):
    assert add(input_str) == expected


def test_missing_number_in_last_position_returns_error():
    assert add("1,3,") == "Number expected but EOF found"


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ["//;\n1;2", "3"],
        ["//|\n1|2|3", "6"],
        ["//sep\n2sep3", "5"],
    ],
)
def test_can_use_custom_delimiters(input_str, expected):
    assert add(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ["//|\n1|2,3", "'|' expected but ',' found at position 3."],
        ["//sep\n1sep2,3", "'sep' expected but ',' found at position 5."],
        ["3,1,5%6", "',' expected but '%' found at position 5."],
        ["3.1,1,5.3%6", "',' expected but '%' found at position 9."],
        ["3,16,51%6", "',' expected but '%' found at position 7."],
    ],
)
def test_invalid_delimiter_returns_error(input_str, expected):
    assert add(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ["-1,2", "Negative not allowed : -1"],
        ["2,-4,-5", "Negative not allowed : -4, -5"],
        ["3,4,-7", "Negative not allowed : -7"],
        ["3.5,-6.2", "Negative not allowed : -6.2"],
    ],
)
def test_negative_numbers_not_allowed(input_str, expected):
    assert add(input_str) == expected
