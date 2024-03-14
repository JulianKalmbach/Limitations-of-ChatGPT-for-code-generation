from enum import Enum, auto

class MyState(Enum):
    INIT = auto()
    LIGHT_ON = auto()
    SCREEN_ON = auto()
    SCREEN_LIGHT_ON = auto()

def next_state(state: MyState, input: str) -> MyState:
    if state == MyState.INIT:
        if input == "SENS_ACC":
            return MyState.LIGHT_ON
        elif input == "SENS_TAP":
            return MyState.SCREEN_ON
    elif state == MyState.LIGHT_ON:
        if input == "SENS_ACC":
            return MyState.INIT
        elif input == "SENS_TAP":
            return MyState.SCREEN_LIGHT_ON
    elif state == MyState.SCREEN_ON:
        if input == "SENS_ACC":
            return MyState.SCREEN_LIGHT_ON
        elif input == "SENS_TAP":
            return MyState.INIT
    elif state == MyState.SCREEN_LIGHT_ON:
        if input == "SENS_ACC" or input == "SENS_TAP":
            return MyState.INIT
    # Bei ungültigen Signalen den aktuellen Zustand beibehalten
    return state


from typing import TypeVar, Generic, Iterable

# Definition der Zustände als TypeVar
S = TypeVar('S', bound='State')


class State(Generic[S]):
    def next(self, input: str) -> 'State[S]':
        raise NotImplementedError

    def output(self) -> MyState:
        raise NotImplementedError


class S_Init(State['S_Init']):
    acc_count = 0
    tap_count = 0

    def next(self, input: str) -> State:
        if input == "SENS_ACC":
            self.acc_count += 1
            if self.acc_count == 2:
                return S_LightOn()
        elif input == "SENS_TAP":
            self.tap_count += 1
            if self.tap_count == 2:
                return S_ScreenOn()
        else:
            self.acc_count = 0
            self.tap_count = 0
        return self

    def output(self) -> MyState:
        return MyState.INIT


class S_LightOn(State['S_LightOn']):
    # Implementierung für LIGHT_ON-Zustand...
    pass


class S_ScreenOn(State['S_ScreenOn']):
    # Implementierung für SCREEN_ON-Zustand...
    pass


class S_ScreenLightOn(State['S_ScreenLightOn']):
    # Implementierung für SCREEN_LIGHT_ON-Zustand...
    pass


# Implementierung der anderen Zustände entsprechend...

def automaton(input: Iterable[str]):
    state: State[S] = S_Init()

    # Erstes Output vor der Schleife
    yield state.output()

    for x in input:
        state = state.next(x)
        yield state.output()

# Beispielaufruf der automaton Funktion
#list(automaton(["SENS_ACC", "SENS_ACC", "SENS_TAP", "SENS_TAP"]))
