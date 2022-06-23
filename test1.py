import math
import pytest


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_square():
    num = 7
    assert 7 * 7 == 40


def test_quality():
    assert 10 == 11


def fetch_func_one():
    t = 5
    # assert reuse_func[1][0] / reuse_func[0] == t, "Comparison Passed"
    return


def fetch_func_two(reuse_func):
    t = 20
    assert reuse_func[1][1] / reuse_func[0] == t, "Comparison Failed"
