from ..fuel import gauge, convert
import pytest

def test_exception_causes():
    with pytest.raises(ValueError):
        assert gauge(3, 2) is ValueError
    with pytest.raises(ZeroDivisionError):
        assert gauge(0, 2) is ZeroDivisionError
    with pytest.raises(ValueError):
        assert gauge(3, 0) is ValueError
    with pytest.raises(ZeroDivisionError):
        assert gauge(-2, 1) is ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        assert gauge(0, 0) is ZeroDivisionError


def test_convert():
    assert convert("1/4") == (1, 4)
    assert convert("0/4") == (0, 4)
    assert convert("-2/3") == (-2, 3)
    assert convert("6/7") == (6, 7)
    assert convert("2/8") == (2, 8)

def test_percentage():
    assert gauge(2, 4) == "50.0%"
    assert gauge(1, 3) == "33.33%"
    assert gauge(3, 4) == "75.0%"
    assert gauge(1, 1000) == "E"
    assert gauge(100, 100) == "F"

#exception_causes()
#E_or_F()
#percentage()