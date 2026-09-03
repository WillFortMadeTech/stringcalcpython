from string_calculator import add


def test_add_is_wired_up():
    # Given / When
    result = add("")

    # Then
    assert result is True
