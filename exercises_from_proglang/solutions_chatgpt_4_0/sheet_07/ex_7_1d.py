from typing import Optional
from exercises_from_proglang.solutions_chatgpt_4_0.sheet_07.tree import Node, Op, OpSym, Val, Var

def optimize_step_if(e: Node) -> Optional[Node]:
    if isinstance(e, Op) and isinstance(e.left, Val) and isinstance(e.right, Val) and e.sym == OpSym.MUL:
        return Val(e.left.value * e.right.value)
    if isinstance(e, Op) and isinstance(e.left, Var) and isinstance(e.right, Var) and e.left.name == e.right.name and e.sym == OpSym.ADD:
        return Op(OpSym.MUL, Val(2), e.left)
    if isinstance(e, Op) and e.left == e.right and e.sym == OpSym.ADD:
        return Op(OpSym.MUL, Val(2), e.left)
    if isinstance(e, Op) and isinstance(e.left, Op) and e.left.sym == e.sym:
        return Op(e.sym, e.left.left, Op(e.sym, e.left.right, e.right))
    if isinstance(e, Op):
        new_left = optimize_step_if(e.left)
        if new_left:
            return Op(e.sym, new_left, e.right)
        new_right = optimize_step_if(e.right)
        if new_right:
            return Op(e.sym, e.left, new_right)
    return None