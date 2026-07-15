from src.main import add


def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0
