from dataclasses import dataclass
from typing import Optional
from enum import Enum


class OpSym(Enum):
    ADD = "+"
    MUL = "*"


@dataclass
class Var:
    name: str


@dataclass
class Val:
    value: int


@dataclass
class Op:
    sym: OpSym
    left: 'Node'
    right: 'Node'


Node = Var | Val | Op
