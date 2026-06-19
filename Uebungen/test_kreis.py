import math
import pytest
from Uebungen.kreis_funktionen2 import calc_diameter, circumference, calc_area


def test_durchmesser():
    assert calc_diameter(5) == 10


def test_umfang():
    assert circumference(1) == pytest.approx(2 * math.pi)


def test_flaeche():
    assert calc_area(2) == pytest.approx(4 * math.pi)