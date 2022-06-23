import pytest


# Method that we want to reuse
@pytest.fixture
def reuse_func():
    speed = 20
    dist = [100, 200]
    return [speed, dist]


def fetch_func_one(reuse_func):
    t = 5
    assert reuse_func[1][0] / reuse_func[0] == t, "Comparison Passed"


def fetch_func_two(reuse_func):
    t = 20
    assert reuse_func[1][1] / reuse_func[0] == t, "Comparison Failed"
