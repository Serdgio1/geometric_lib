import pytest
from square import area, perimeter


def test_square_area():
    assert area(5) == 25
    assert area(0) == 0
    assert area(1) == 1


def test_square_perimeter():
    assert perimeter(5) == 20
    assert perimeter(0) == 0
    assert perimeter(1) == 4


def test_square_negative_side():
    with pytest.raises(ValueError):
        area(-1)
    with pytest.raises(ValueError):
        perimeter(-1)
