from typing import Any, Callable


def suppress(f: Callable[[], Any], ignore: tuple) -> Callable[[], Any]:
    def wrapped_f():
        try:
            return f()
        except ignore:
            return None
    return wrapped_f
