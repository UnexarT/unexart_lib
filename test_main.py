import main
import numpy

def test_add():
    assert main.add(1, 2) == 3
    assert main.add(-1, 1) == 0
    assert main.add(-1, -1) == -2
    assert main.add(-1, 0) == -1
    #assert main.add(0, 0) == 0
