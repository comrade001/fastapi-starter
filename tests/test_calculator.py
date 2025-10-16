from hello_python.calculator import Calculator, Operation, Op
import pytest


def test_add():
    calc = Calculator()
    op = Operation(Op.ADD, (1.0, 2.5, 3.5))
    assert calc.evaluate(op) == pytest.approx(7.0)


def test_sqr():
    calc = Calculator()
    op = Operation(Op.SQR, (2.0, 2.0))
    assert calc.evaluate(op) == pytest.approx(4.0)


def test_sub():
    calc = Calculator()
    op = Operation(Op.SUB, (10.0, 4.0, 1.0))
    assert calc.evaluate(op) == pytest.approx(5.0)


def test_mul():
    calc = Calculator()
    op = Operation(Op.MUL, (2.0, 3.0, 4.0))
    assert calc.evaluate(op) == pytest.approx(24.0)


def test_div():
    calc = Calculator()
    op = Operation(Op.DIV, (20.0, 2.0, 2.0))
    assert calc.evaluate(op) == pytest.approx(5.0)


def test_div_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.evaluate(Operation(Op.DIV, (10.0, 0.0)))


def test_validation_rules():
    with pytest.raises(ValueError):
        Operation(Op.ADD, ())
    with pytest.raises(ValueError):
        Operation(Op.SUB, (1.0,))
    with pytest.raises(ValueError):
        Operation(Op.DIV, (1.0,))
    with pytest.raises(ValueError):
        Operation(Op.SQR, (2.0, 1.0, 2.0))
