from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from functools import reduce
from typing import Iterable


class Op(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    SQR = auto()


@dataclass(frozen=True)
class Operation:
    op: Op
    operands: tuple[float, ...]

    def __post_init__(self) -> None:
        if len(self.operands) == 0:
            raise ValueError("operands must not be empty")
        if self.op in (Op.SUB, Op.DIV, Op.SQR) and len(self.operands) < 2:
            raise ValueError(f"{self.op.name} requires at leats two operands")
        if self.op is Op.SQR and len(self.operands) != 2:
            raise ValueError("SQR requieres exacly two operands")


class Calculator:
    def evaluate(self, operation: Operation) -> float:
        op = operation.op
        nums = operation.operands
        if op is Op.ADD:
            return self._add(nums)
        if op is Op.SQR:
            return self._sqr(nums)
        if op is Op.SUB:
            return self._sub(nums)
        if op is Op.MUL:
            return self._mul(nums)
        if op is Op.DIV:
            return self._div(nums)
        raise ValueError("unsupported operation")

    @staticmethod
    def _add(nums: Iterable[float]) -> float:
        total = 0.0
        for n in nums:
            total += n
        return total

    @staticmethod
    def _sub(nums: tuple[float, ...]) -> float:
        head, *tail = nums
        result = head
        for n in tail:
            result -= n
        return result

    @staticmethod
    def _div(nums: tuple[float, ...]) -> float:
        head, *tail = nums
        result = head
        for n in tail:
            if n == 0.0:
                raise ZeroDivisionError("division by zero")
            result /= n
        return result

    @staticmethod
    def _mul(nums: Iterable[float]) -> float:
        return reduce(lambda a, b: a * b, nums, 1.0)

    @staticmethod
    def _sqr(nums: tuple[float, ...]) -> float:
        base, exp = nums
        return base**exp
