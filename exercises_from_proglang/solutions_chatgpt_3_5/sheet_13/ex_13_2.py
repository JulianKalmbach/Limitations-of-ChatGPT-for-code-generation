from typing import TypeVar, Generic, Iterable
from enum import Enum, auto

S = TypeVar('S')

class State(Generic[S, Enum]):
    def next(self, input: str) -> S:
        raise NotImplementedError("Subclasses must implement next method.")

    def output(self) -> Enum:
        raise NotImplementedError("Subclasses must implement output method.")

class S_Init(State['S_Init', 'MyState']):
    def next(self, input: str) -> S:
        if input == "SENS_ACC":
            return S_AfterAcc().next(input)
        elif input == "SENS_TAP":
            return S_AfterTap().next(input)
        else:
            return self

    def output(self) -> Enum:
        return MyState.INIT

class S_AfterAcc(State['S_AfterAcc', 'MyState']):
    def __init__(self):
        self.count = 1

    def next(self, input: str) -> S:
        if input == "SENS_ACC":
            self.count += 1
            if self.count == 2:
                return MyState.LIGHT_ON
            elif self.count > 2:
                return S_Init().next(input)
        else:
            self.count = 1
        return self

    def output(self) -> Enum:
        return MyState.INIT

class S_AfterTap(State['S_AfterTap', 'MyState']):
    def __init__(self):
        self.count = 1

    def next(self, input: str) -> S:
        if input == "SENS_TAP":
            self.count += 1
            if self.count == 2:
                return MyState.SCREEN_ON
            elif self.count > 2:
                return S_Init().next(input)
        else:
            self.count = 1
        return self

    def output(self) -> Enum:
        return MyState.INIT

class MyState(Enum):
    INIT = auto()
    LIGHT_ON = auto()
    SCREEN_ON = auto()
    SCREEN_LIGHT_ON = auto()

    def __str__(self):
        return self.name

def automaton(input: Iterable[str]):
    state: State[S | str, S] = S_Init()

    yield state.output()

    for x in input:
        state = state.next(x)
        yield state.output()

# Testen der Zustandsmaschine
input_data = ["SENS_ACC", "SENS_ACC", "SENS_TAP", "SENS_TAP", "SENS_TAP", "SENS_ACC", "SENS_ACC", "SENS_TAP", "SENS_TAP"]
for state in automaton(input_data):
    print(state)
