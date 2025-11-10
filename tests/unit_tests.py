from src.main import add,sub

def test_add():
    assert add(2,3)==5
    assert add(5,3)==8
    assert add(12,1)==13


def test_sub():
    assert sub(5,3)==2
    assert sub(15,2)==13
    assert sub(-2,-1)==-3
    