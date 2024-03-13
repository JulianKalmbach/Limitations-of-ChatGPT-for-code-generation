from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.tree import Var, Val, Op, OpSym
from typing import Union

def node_to_str(node: Union[Var, Val, Op]) -> str:
    if isinstance(node, Var):
        return node.name
    elif isinstance(node, Val):
        return str(node.value)
    elif isinstance(node, Op):
        left_str = node_to_str(node.left)
        right_str = node_to_str(node.right)
        return f"({left_str} {node.sym.value} {right_str})"

# Test
e = Op(OpSym.ADD, Op(OpSym.MUL, Val(2), Var('x')), Val(5))
assert node_to_str(e) == '((2 * x) + 5)'
assert node_to_str(Var('x')) == 'x'
assert node_to_str(Val(2)) == '2'

def node_to_str_if(node: Union[Var, Val, Op]) -> str:
    if isinstance(node, Var):
        return node.name
    if isinstance(node, Val):
        return str(node.value)
    if isinstance(node, Op):
        left_str = node_to_str_if(node.left)
        right_str = node_to_str_if(node.right)
        return "(" + left_str + " " + node.sym.value + " " + right_str + ")"

# Test
e = Op(OpSym.ADD, Op(OpSym.MUL, Val(2), Var('x')), Val(5))
assert node_to_str_if(e) == '((2 * x) + 5)'
assert node_to_str_if(Var('x')) == 'x'
assert node_to_str_if(Val(2)) == '2'