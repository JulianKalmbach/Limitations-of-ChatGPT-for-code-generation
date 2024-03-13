from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.tree import Var, Val, Op, OpSym
from typing import Optional, Union


def optimize_step_if(e: Union[Var, Val, Op]) -> Optional[Union[Var, Val, Op]]:
    if isinstance(e, Op):
        if isinstance(e.left, Val) and isinstance(e.right, Val):
            if e.sym == OpSym.ADD:
                return Val(e.left.value + e.right.value)
            elif e.sym == OpSym.MUL:
                return Val(e.left.value * e.right.value)
        elif e.sym == OpSym.ADD or e.sym == OpSym.MUL:
            if e.left == e.right:
                if e.sym == OpSym.ADD:
                    return Op(OpSym.MUL, Val(2), e.left)
                elif e.sym == OpSym.MUL:
                    return Op(OpSym.MUL, Val(2), e.left)
        left_opt = optimize_step_if(e.left)
        if left_opt:
            return Op(e.sym, left_opt, e.right)
        right_opt = optimize_step_if(e.right)
        if right_opt:
            return Op(e.sym, e.left, right_opt)
    return None


# Test
e1 = Op(OpSym.MUL, Val(2), Val(3))
e2 = Op(OpSym.MUL, Val(3), Val(2))
assert optimize_step_if(Op(OpSym.ADD, e1, e2)) == Op(OpSym.ADD, Val(6), e2)
assert optimize_step_if(Op(OpSym.ADD, Val(6), e2)) == Op(OpSym.ADD, Val(6), Val(6))
assert optimize_step_if(Op(OpSym.ADD, Val(6), Val(6))) == Val(12)
assert optimize_step_if(Val(12)) == None