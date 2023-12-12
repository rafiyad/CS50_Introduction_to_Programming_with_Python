from working import convert
import pytest

def main():
    test_worng_hour()
    test_worng_minute()
    test_worng_input()
    test_right_format()
    test_middle_to()


def test_worng_hour():
    with pytest.raises(ValueError):
        convert("19 AM to 13 PM")

def test_worng_minute():
    with pytest.raises(ValueError):
        convert("9:61 AM to 3:68 PM")

def test_worng_input():
    with pytest.raises(ValueError):
        convert("cat to dog")


def test_right_format():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("4:30 AM to 5:30 PM")=="04:30 to 17:30"
    assert convert("10 PM to 8 AM")=="22:00 to 08:00"

def test_middle_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

if __name__ == "__main__":
    main()
