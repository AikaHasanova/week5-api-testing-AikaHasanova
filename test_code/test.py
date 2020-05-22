from addsimple.adding import add

def test_add():
    given_value=1
    expected=2
    assert add(given_value)==expected

def test_add2():
    given_value=-1
    expected=0
    assert add(given_value)==expected
