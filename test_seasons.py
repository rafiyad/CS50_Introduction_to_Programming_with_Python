from seasons import dob_check

def main():
    test_input_format()

def test_input_format():
    assert dob_check("1999-01-01")==("1999", "01", "01")
    assert dob_check("January 1, 1999")==None
    assert dob_check("1999/01/01")==None


if __name__=="__main__":
    main()
