from exercises_from_proglang.solutions_chatgpt_4_0.sheet_07.tree import Node, Var, Val, Op

def node_to_str(node: Node) -> str:
    match node:
        case Var(name):
            return name
        case Val(value):
            return str(value)
        case Op(sym, left, right):
            return f'({node_to_str(left)} {sym.value} {node_to_str(right)})'

def node_to_str_if(node: Node) -> str:
    if isinstance(node, Var):
        return node.name
    elif isinstance(node, Val):
        return str(node.value)
    elif isinstance(node, Op):
        return f'({node_to_str_if(node.left)} {node.sym.value} {node_to_str_if(node.right)})'