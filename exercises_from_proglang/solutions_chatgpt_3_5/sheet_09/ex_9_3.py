from typing import List


def apply_binary_operator(operator: str, x: float, y: float) -> float:
    match operator:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case _:
            raise ValueError("Unsupported operator")


class Vector:
    def __init__(self, values: List[float]):
        self._values = values

    @property
    def values(self) -> List[float]:
        return self._values

    @property
    def dimension(self) -> int:
        return len(self._values)

    @property
    def len(self) -> float:
        return sum(x ** 2 for x in self._values) ** 0.5

    def __str__(self) -> str:
        return f"{self.dimension}D vector: {self._values}"

    def __pos__(self) -> 'Vector':
        return self

    def __neg__(self) -> 'Vector':
        return Vector([-x for x in self._values])

    def operate_binary(self, operator: str, other) -> 'Vector':
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise ValueError("Vectors must have the same dimension")
            return Vector([apply_binary_operator(operator, x, y) for x, y in zip(self.values, other.values)])
        elif isinstance(other, (int, float)):
            return Vector([apply_binary_operator(operator, x, other) for x in self.values])
        else:
            raise TypeError("Unsupported operand type")

    def __add__(self, other) -> 'Vector':
        return self.operate_binary("+", other)

    def __radd__(self, other) -> 'Vector':
        return self.__add__(other)

    def __sub__(self, other) -> 'Vector':
        return self.operate_binary("-", other)

    def __rsub__(self, other) -> 'Vector':
        return self.__neg__().__add__(other)

    def __mul__(self, other) -> 'Vector':
        return self.operate_binary("*", other)

    def __rmul__(self, other) -> 'Vector':
        return self.__mul__(other)