# two or more method
import pytest
from fuel import convert, gauge
def main():
    test_convert()
    test_gauge()
    test_zero_division()
    test_valueError()


def test_convert():
    assert convert("1/4")==25
    assert convert("1/2")==50
    assert convert("3/4")==75
    assert convert("1/100")==1
    assert convert("99/100")==99

def test_gauge():
    assert gauge(99)=="F"
    assert gauge(100)=="F"
    assert gauge(1)=="E"
    assert gauge(25)=="25%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueError():
    with pytest.raises(ValueError):
        convert("Cat/dog")


if __name__ == "__main__":
    main()
