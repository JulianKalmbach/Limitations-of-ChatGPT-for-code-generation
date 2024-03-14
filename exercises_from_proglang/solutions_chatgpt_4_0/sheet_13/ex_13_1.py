from typing import Callable, Tuple, Type, Any

def suppress(f: Callable[[], Any], ignore: Tuple[Type[BaseException], ...] = ()) -> Callable[[], Any]:
    def g() -> Any:
        try:
            return f()
        except ignore:
            return None
    return g

# Beispielnutzung entsprechend der Aufgabenstellung
from functools import partial

def foo(n: int) -> int:
    return 35 // n

# Dies sollte funktionieren und 35 zurückgeben
assert suppress(partial(foo, 1))() == 35 == foo(1)

# Dies sollte None zurückgeben, da die ZeroDivisionError ignoriert wird
print(suppress(partial(foo, 0), (ZeroDivisionError,))())

# Dies sollte eine ZeroDivisionError auslösen, da keine Ausnahmen ignoriert werden sollen
try:
    suppress(partial(foo, 0))()
except ZeroDivisionError as e:
    print("ZeroDivisionError caught as expected.")
