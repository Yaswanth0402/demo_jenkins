from main import mul, div
 
def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 1) == -1
 
def test_div():
    assert div(10, 5) == 2
    assert div(10, 2) == 5