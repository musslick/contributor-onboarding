from src.utils import modulo
def test_modulo():
    a = 3
    b = 2

    c = 0

    assert modulo(a, b) == 1
    assert modulo(b, a) == 2
    assert modulo(b, b) == 0
    assert modulo(c, b) == 0