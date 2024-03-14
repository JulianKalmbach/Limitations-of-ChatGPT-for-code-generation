from typing import Callable, Tuple

def suppress(f: Callable, ignore: Tuple = ()) -> Callable:
    def g():
        try:
            return f()
        except Exception as e:
            if isinstance(e, ignore):
                return None
            else:
                raise
    return g
