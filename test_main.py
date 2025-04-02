import pytest


def add(a: int, b: int):
    return a + b


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add_param(a, b, expected):
 assert add(a, b) == expected
