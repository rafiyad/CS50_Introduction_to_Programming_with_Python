from bank import value

def main():
    test_firstWord_Hello()
    test_firstWord_H_h()
    test_with_out_H_h()

def test_firstWord_Hello():
    assert value(" Hello")==0
    assert value("  Hello  ")==0
    assert value("  HELLO  ")==0
    assert value("HELLO")==0
    assert value("HeLlO")==0
    assert value("Hello, Newman")==0


def test_firstWord_H_h():
    assert value("How you doing?")==20
    assert value("  How you doing?    ")==20
    assert value("how you doning")==20
    assert value("How's it going?")==20


def test_with_out_H_h():
    assert value("What’s up")==100
    assert value("What's happening?")==100
    assert value("  what's happening?  ")==100
    assert value("where is the manager")==100
    assert value("")==100

if __name__=="__main__":
     main()
