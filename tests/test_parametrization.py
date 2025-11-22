import pytest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_number(number: int):
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_number(number: int, expected: int):
    assert number ** 2 == expected