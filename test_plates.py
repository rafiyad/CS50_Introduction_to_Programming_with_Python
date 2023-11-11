from plates import is_valid
def main():
    test_length()
    test_with_two_alpha()
    test_num_middel()
    test_num_zero()
    test_symbol()



def test_length():
    assert is_valid("AA")==True
    assert is_valid("AAeghg")==True
    assert is_valid("A")==False
    assert is_valid("HJLHNGH")==False

def test_with_two_alpha():
    assert is_valid("HJ")==True
    assert is_valid("H2")==False
    assert is_valid("5H")==False
    assert is_valid("56")==False

def test_num_middel():
    assert is_valid("AAA222")==True
    assert is_valid("AAA22A")==False
    assert is_valid("AA2S2")==False

def test_num_zero():
    assert is_valid("CS50")==True
    assert is_valid("CS05")==False

def test_symbol():
    assert is_valid("CSS.5")==False
    assert is_valid("AA2!")==False



if __name__=="__main__":
    main()

