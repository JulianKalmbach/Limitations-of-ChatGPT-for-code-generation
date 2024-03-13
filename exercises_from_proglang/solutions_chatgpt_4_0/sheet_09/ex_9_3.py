from dataclasses import dataclass, field
from typing import List
import math


def apply_binary_operator(operator: str, a: float, b: float) -> float:
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case _:
            raise ValueError(f"Unbekannter Operator: {operator}")


@dataclass(frozen=True)
class Vector:
    values: List[float] = field(default_factory=list)

    def __post_init__(self):
        if len(self.values) == 0:
            raise ValueError("Dimension muss größer als 0 sein")
        object.__setattr__(self, 'values', tuple(self.values))  # Make values immutable

    @property
    def dimension(self) -> int:
        return len(self.values)

    @property
    def len(self) -> float:
        return math.sqrt(sum(x ** 2 for x in self.values))

    def __str__(self) -> str:
        return f"{self.dimension}D vector: {self.values}"

    def __pos__(self):
        return self

    def __neg__(self):
        return Vector([-x for x in self.values])

    def operate_binary(self, operator: str, other):
        if isinstance(other, (int, float)):
            new_values = [apply_binary_operator(operator, x, other) for x in self.values]
        elif isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise ValueError("Dimensionen stimmen nicht überein")
            new_values = [apply_binary_operator(operator, x, y) for x, y in zip(self.values, other.values)]
        else:
            raise TypeError("Der Operator wird nicht unterstützt")
        return Vector(new_values)

    def __add__(self, other):
        return self.operate_binary("+", other)

    def __sub__(self, other):
        return self.operate_binary("-", other)

    def __mul__(self, other):
        return self.operate_binary("*", other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return Vector([-x for x in self.values]).__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)
