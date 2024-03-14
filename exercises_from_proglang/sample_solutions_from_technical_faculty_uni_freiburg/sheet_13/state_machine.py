from enum import Enum, auto

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Iterable, TypeVar


# Part a) and b).
class MyState(Enum):
    INIT = auto()
    LIGHT_ON = auto()
    SCREEN_ON = auto()
    SCREEN_LIGHT_ON = auto()

    INIT_ACC = auto()
    LIGHT_ON_ACC = auto()
    SCREEN_ON_ACC = auto()
    SCREEN_LIGHT_ON_ACC = auto()

    INIT_TAP = auto()
    LIGHT_ON_TAP = auto()
    SCREEN_ON_TAP = auto()
    SCREEN_LIGHT_ON_TAP = auto()


S = MyState


def next_state(state: S, sensor_input: str) -> S:
    match sensor_input:
        case "SENS_ACC":
            match state:
                # Invalid combinations.
                case S.INIT_TAP:
                    return S.INIT
                case S.LIGHT_ON_TAP:
                    return S.LIGHT_ON
                case S.SCREEN_ON_TAP:
                    return S.SCREEN_ON
                case S.SCREEN_LIGHT_ON_TAP:
                    return S.SCREEN_LIGHT_ON
                # Now the valid combinations for "in-between" states.
                case S.INIT:
                    return S.INIT_ACC
                case S.LIGHT_ON:
                    return S.LIGHT_ON_ACC
                case S.SCREEN_ON:
                    return S.SCREEN_ON_ACC
                case S.SCREEN_LIGHT_ON:
                    return S.SCREEN_LIGHT_ON_ACC
                # Edges to msin states.
                case S.INIT_ACC:
                    return S.LIGHT_ON
                case S.LIGHT_ON_ACC:
                    return S.INIT
                case S.SCREEN_ON_ACC:
                    return S.SCREEN_LIGHT_ON
                case S.SCREEN_LIGHT_ON_ACC:
                    return S.SCREEN_ON
        case "SENS_TAP":
            match state:
                # Invalid combinations.
                case S.INIT_ACC:
                    return S.INIT
                case S.LIGHT_ON_ACC:
                    return S.LIGHT_ON
                case S.SCREEN_ON_ACC:
                    return S.SCREEN_ON
                case S.SCREEN_LIGHT_ON_ACC:
                    return S.SCREEN_LIGHT_ON
                # Now the valid combinations for "in-between" states.
                case S.INIT:
                    return S.INIT_TAP
                case S.LIGHT_ON:
                    return S.LIGHT_ON_TAP
                case S.SCREEN_ON:
                    return S.SCREEN_ON_TAP
                case S.SCREEN_LIGHT_ON:
                    return S.SCREEN_LIGHT_ON_TAP
                # Edges to msin states.
                case S.INIT_TAP:
                    return S.SCREEN_ON
                case S.LIGHT_ON_TAP:
                    return S.SCREEN_LIGHT_ON
                case S.SCREEN_ON_TAP:
                    return S.INIT
                case S.SCREEN_LIGHT_ON_TAP:
                    return S.LIGHT_ON
        # Invalid input, back to last state.
        case _:
            return state


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


@dataclass
class S_After(State[S | str, S]):
    prefix: list[S | str]

    def next(self, sensor_input: str) -> State[str, S]:
        self.prefix = self.prefix + [sensor_input]
        match self.prefix[-2:]:
            # All invalid states, return the last valid one.
            case ["SENS_ACC", "SENS_TAP"] | ["SENS_TAP", "SENS_ACC"]:
                return S_After(self.prefix[:-2])
            # Now all the valid states.
            case ["SENS_ACC", "SENS_ACC"]:
                match self.prefix[-3]:
                    case S.INIT:
                        return S_After([S.LIGHT_ON])
                    case S.LIGHT_ON:
                        return S_After([S.INIT])
                    case S.SCREEN_ON:
                        return S_After([S.SCREEN_LIGHT_ON])
                    case S.SCREEN_LIGHT_ON:
                        return S_After([S.SCREEN_ON])
            case ["SENS_TAP", "SENS_TAP"]:
                match self.prefix[-3]:
                    case S.INIT:
                        return S_After([S.SCREEN_ON])
                    case S.LIGHT_ON:
                        return S_After([S.SCREEN_LIGHT_ON])
                    case S.SCREEN_ON:
                        return S_After([S.INIT])
                    case S.SCREEN_LIGHT_ON:
                        return S_After([S.LIGHT_ON])
        match self.prefix:
            # "In-between" states.
            case ([S.INIT, _] | [S.LIGHT_ON, _]
                    | [S.SCREEN_ON, _] | [S.SCREEN_LIGHT_ON, _]):
                return self

    def output(self) -> S:
        # This is can be only one of the "main" states.
        if len(self.prefix) == 1:
            return self.prefix[0]

        # Now only "main" states + SENS_ACC or + SENS_TAP exist (not both!).
        # We use the __getitem__ method from Enum and construct the new name,
        # to return a S (i.e. MyState).
        return S[f"{self.prefix[0].name}_{self.prefix[1].split('_')[-1]}"]


@dataclass
class S_Init(State[S | str, S]):
    def next(self, sensor_input: str) -> State[S | str, S]:
        match sensor_input:
            case "SENS_ACC" | "SENS_TAP":
                return S_After([S.INIT, sensor_input])
        return S_After([S.INIT])

    def output(self) -> S:
        return S.INIT


def automaton(input: Iterable[str]):
    state: State[S | str, S] = S_Init()

    yield state.output()
    for x in input:
        state = state.next(x)
        yield state.output()
