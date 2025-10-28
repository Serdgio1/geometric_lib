import pytest
from circle import area, perimeter


def test_circle_area():
    assert area(5) == pytest.approx(78.54, rel=1e-2)
    assert area(0) == 0
    assert area(1) == pytest.approx(3.14, rel=1e-2)


def test_circle_perimeter():
    assert perimeter(5) == pytest.approx(31.42, rel=1e-2)
    assert perimeter(0) == 0
    assert perimeter(1) == pytest.approx(6.28, rel=1e-2)


def test_circle_negative_radius():
    with pytest.raises(ValueError):
        area(-1)
    with pytest.raises(ValueError):
        perimeter(-1)
