from src.math_ops import add, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(3, 4) == 7


def test_subtrac():
    assert subtract(2, 1) == 1
    assert subtract(3, 2) == 1
    assert subtract(4, 3) == 1
    assert subtract(-4, 3) == -7
    assert subtract(4, -3) == 7
