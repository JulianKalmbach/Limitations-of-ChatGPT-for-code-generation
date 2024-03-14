from typing import Callable
import math

import pytest


def differentiate(f: Callable[[float], float], h: float) -> Callable[[float], float]:
    def central_difference(x_0):
        return (f(x_0 + h) - f(x_0 - h)) / (2 * h)
    return central_difference

# Test
def test_differentiate():
    f = lambda x: 1 / 2 * x ** 2
    h = 1e-2
    diff_func = differentiate(f, h)
    assert diff_func(0) == pytest.approx(0.0)

test_differentiate()

def integrate(f: Callable[[float], float], n: int) -> Callable[[float, float], float]:
    def simpson_rule(a, b):
        h = (b - a) / n
        x_i = [a + i * h for i in range(n + 1)]
        s_i = [(h / 6) * (f(x_i[i]) + 4 * f((x_i[i] + x_i[i+1]) / 2) + f(x_i[i+1])) for i in range(n)]
        return sum(s_i)
    return simpson_rule

# Test
def test_integrate():
    f = lambda x: math.exp(x)
    n = 5
    integral_func = integrate(f, n)
    assert integral_func(0, 1) == pytest.approx(math.exp(1) - 1)

test_integrate()


def test_differentiate():
    # Testfall für differentiate-Funktion
    f = lambda x: 1 / 2 * x ** 2
    h = 1e-2
    diff_func = differentiate(f, h)
    assert diff_func(0) == pytest.approx(0.0)

def test_integrate():
    # Testfall für integrate-Funktion
    f = lambda x: math.exp(x)
    n = 5
    integral_func = integrate(f, n)
    assert integral_func(0, 1) == pytest.approx(math.exp(1) - 1)

# Führe Tests aus
pytest.main([__file__])


