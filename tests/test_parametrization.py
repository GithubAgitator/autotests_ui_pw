import pytest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
@pytest.mark.xfail
def test_number(number: int):
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
@pytest.mark.xfail
def test_several_number(number: int, expected: int):
    assert number ** 2 == expected