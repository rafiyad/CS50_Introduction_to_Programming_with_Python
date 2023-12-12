from um import count
import pytest

def main():
    test_one_um()
    test_two_um()
    test_three_um()



def test_one_um():
    assert count("Hello, um, world")==1
    assert count("I am Um, rule the world")==1
    assert count("um?")==1

def test_two_um():
    assert count("Um, thanks, um...")==2
    assert count("..um...I am learing python um..")==2

def test_three_um():
    assert count("Um, um thanks, um...")==3
    assert count("..um...I am learing Um python um..")==3

def test_with_word():
    assert count("yummy")==0


if __name__ == "__main__":
    main()

