import sample5
import pytest

def test_sample5():
    assert sample5.div2(1.2, 0.6) == 2.0

def test_sample5_zero():
    with pytest.raises(ZeroDivisionError):
        sample5.div2(1.2, 0.0)