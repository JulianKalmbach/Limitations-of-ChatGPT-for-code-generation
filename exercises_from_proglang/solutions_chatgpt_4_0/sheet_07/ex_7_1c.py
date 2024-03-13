from typing import Optional
from exercises_from_proglang.solutions_chatgpt_4_0.sheet_07.tree import Node, Op, OpSym, Val, Var

def optimize_step(e: Node) -> Optional[Node]:
    match e:
        case Op(OpSym.MUL, Val(a), Val(b)):
            return Val(a * b)
        case Op(OpSym.ADD, Var(a), Var(b)) if a == b:
            return Op(OpSym.MUL, Val(2), Var(a))
        case Op(OpSym.ADD, left, right) if left == right:
            return Op(OpSym.MUL, Val(2), left)
        case Op(sym, Op(left_sym, left_left, left_right), right) if sym == left_sym:
            return Op(sym, left_left, Op(sym, left_right, right))
        case Op(sym, left, right):
            new_left = optimize_step(left)
            if new_left is not None:
                return Op(sym, new_left, right)
            new_right = optimize_step(right)
            if new_right is not None:
                return Op(sym, left, new_right)
    return None