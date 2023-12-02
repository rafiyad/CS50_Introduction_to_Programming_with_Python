from numb3rs import validate

def main():
    test_validate_format()
    test_validate_range()
    test_validate_words()



def test_validate_format():
    assert validate(r"127.0.0.1")==True
    assert validate(r"255.255.255.255")==True
    assert validate(r"255.24.04")==False
    assert validate(r"253.22")==False
    assert validate(r"0")==False


def test_validate_range():
    assert validate("255.255.255.255")==True
    assert validate("257.255.255.255")==False
    assert validate("257.258.255.255")==False
    assert validate("257.259.258.255")==False
    assert validate("257.265.285.289")==False
    assert validate("512.2.45.5")==False
    assert validate("12.622.45.5")==False

def test_validate_words():
    assert validate("cat")==False
    assert validate("cat.dog")==False


if __name__=="__main__":
    main()
