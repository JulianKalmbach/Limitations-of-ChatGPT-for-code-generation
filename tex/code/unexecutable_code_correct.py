# Base class for all states.
INPUT = TypeVar("INPUT")
OUTPUT = TypeVar("OUTPUT")

@dataclass
class State(Generic[INPUT, OUTPUT], ABC):
    def next(self, sensor_input: INPUT) -> 'State':
        return self

    @abstractmethod
    def output(self) -> OUTPUT:
        ...