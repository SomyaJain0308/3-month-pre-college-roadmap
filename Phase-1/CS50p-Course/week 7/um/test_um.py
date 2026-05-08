from um import count

def test_idk():
    assert count("um")==1

def test_basic():
    assert count("um") == 1

def test_multiple():
    assert count("um um um") == 3

def test_case_insensitive():
    assert count("Um UM uM") == 3

def test_yummy_excluded():
    assert count("yummy") == 0

def test_umm_excluded():
    assert count("umm") == 0

def test_mixed():
    assert count("Um, yummy food, um I was like umm going") == 2

def test_empty():
    assert count("") == 0

def test_no_ums():
    assert count("hello world") == 0

