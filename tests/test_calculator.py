import pytest

from calculator import Calculator


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0.5, 0.5, 1.0)])
def test_add(a, b, expected):
    assert Calculator(a, b).add() == expected


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator(5, 0).div()
