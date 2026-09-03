from string_calculator import add


def test_add_with_empty_string_returns_zero():
    # Given / When
    result = add("")

    # Then
    assert result is "0"
