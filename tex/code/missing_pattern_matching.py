def node_to_str(node: Union[Var, Val, Op]) -> str:
    if isinstance(node, Var):
        return node.name
    elif isinstance(node, Val):
        return str(node.value)
    elif isinstance(node, Op):
        left_str = node_to_str(node.left)
        right_str = node_to_str(node.right)
        return f"({left_str} {node.sym.value} {right_str})"