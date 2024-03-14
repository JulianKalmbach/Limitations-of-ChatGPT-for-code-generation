from typing import Callable


def differentiate(f: Callable[[float], float], h: float) -> Callable[[float], float]:
    return lambda x_0: (f(x_0 + h) - f(x_0 - h)) / (2 * h)

def integrate(f: Callable[[float], float], n: int) -> Callable[[float, float], float]:
    def integral(a: float, b: float) -> float:
        h = (b - a) / n
        result = 0
        for i in range(n):
            x_i = a + i * h
            x_ip1 = x_i + h
            result += (h / 6) * (f(x_i) + 4 * f((x_i + x_ip1) / 2) + f(x_ip1))
        return result
    return integral

import math

# Testfunktion: f(x) = 1/2 * x^2, deren Ableitung ist f'(x) = x
f = lambda x: 1/2 * x ** 2
df = differentiate(f, 1e-4)  # Sehr kleine Schrittweite für eine genauere Approximation
assert math.isclose(df(1), 1, rel_tol=1e-3), "Test für differentiate fehlgeschlagen"

# Das Ergebnis sollte nahe bei 1 liegen, was der Ableitung von f(x) = 1/2 * x^2 bei x = 1 entspricht.

# Testfunktion: f(x) = e^x, deren Integral über das Intervall [0, 1] ist e - 1
f = math.exp
integral_f = integrate(f, 1000)  # Verwende eine hohe Anzahl an Schritten für eine genauere Approximation
assert math.isclose(integral_f(0, 1), math.exp(1) - 1, rel_tol=1e-3), "Test für integrate fehlgeschlagen"

# Das Ergebnis sollte nahe bei e - 1 liegen, was dem bestimmten Integral von f(x) = e^x über [0, 1] entspricht.
