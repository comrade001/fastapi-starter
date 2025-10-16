import time
from hello_python.timer import Timer, Dummy, Suppressor, SpySuppressor, NoSuppress
import pytest


def test_timer_measures_sleep():
    with Timer() as t:
        time.sleep(1.0)
    assert 0.9 <= t.elapsed <= 1.2


def test_contextmanager_returns_cero():
    with Dummy() as d:
        print("algo")
    assert d == 0


def test_suppresed_exception():
    with Suppressor():
        ValueError("boom")
    assert True


def test_exit_receives_exception():
    s = SpySuppressor()
    with s:
        raise ValueError("boom")
    assert s.args[0] is ValueError
    assert str(s.args[1]) == "boom"


def test_not_suppressed():
    with pytest.raises(ZeroDivisionError):
        with NoSuppress():
            1 / 0
