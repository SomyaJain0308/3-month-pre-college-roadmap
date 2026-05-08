from numb3rs import validate


def test_alpha():
    assert validate("cat")==False


def test_numbers():
    assert validate("1.1.1.1")==True
    assert validate("256.256.256.256")==False
    assert validate("2.256.3.4")==False


