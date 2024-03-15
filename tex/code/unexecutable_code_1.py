S = TypeVar('S')

class State(Generic[S, Enum]):
    def next(self, input: str) -> S:
        raise NotImplementedError("Subclasses must implement next method.")

    def output(self) -> Enum:
        raise NotImplementedError("Subclasses must implement output method.")