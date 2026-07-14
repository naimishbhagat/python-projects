from app.demo import add,sub,mul,div
import pytest
@pytest.mark.skip("Skipping the test for some reason")
def test_add():
    assert add(10,20) == 30

def test_sub():
    assert sub(10,20) == -10

def test_mul():
    assert mul(10,20) == 200

def test_div():
    assert div(10,20) == 0.5

    #case for asserting exception
    with pytest.raises(ValueError):
        div(4,0)