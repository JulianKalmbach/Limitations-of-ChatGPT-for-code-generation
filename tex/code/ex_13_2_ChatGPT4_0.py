S = TypeVar('S', bound='State')

class State(Generic[S]):
    def next(self, input: str) -> 'State[S]':
        raise NotImplementedError

    def output(self) -> MyState:
        raise NotImplementedError