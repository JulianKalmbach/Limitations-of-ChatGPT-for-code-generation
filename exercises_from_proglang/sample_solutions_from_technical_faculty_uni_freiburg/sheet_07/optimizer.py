from typing import Optional
from tree import Node, Val, Var, Op, OpSym
from parser import parse  # (s: str) -> Optional[Node]


def node_to_str(e: Node) -> str:
    match e:
        case Val(i):
            return str(i)
        case Var(x):
            return x
        case Op(op, left, right):
            return ('(' + node_to_str(left) +
                    ' ' + op.value +
                    ' ' + node_to_str(right) +
                    ')')
        case _:
            raise Exception("unreachable")


def node_to_str_if(e: Node) -> str:
    if type(e) is Val:
        return str(e.value)
    elif type(e) is Var:
        return e.name
    elif type(e) is Op:
        return ('(' + node_to_str_if(e.left) +
                ' ' + e.sym.value +
                ' ' + node_to_str_if(e.right) +
                ')')
    else:
        raise Exception("unreachable")


def optimize_step(e: Node) -> Optional[Node]:
    match e:
        # Evaluation of constants ("Constant Folding")
        case Op(OpSym.ADD, Val(v1), Val(v2)):
            return Val(v1 + v2)
        case Op(OpSym.MUL, Val(v1), Val(v2)):
            return Val(v1 * v2)

        # e + e  →  2 * e  ("Common sub-expression elimination")
        case Op(OpSym.ADD, e1, e2) if e1 == e2:
            return Op(OpSym.MUL, Val(2), e1)

        # e1 + (e2 + e3)  →  (e1 + e2) + e3  ("Associativity of +")
        # e1 * (e2 * e3)  →  (e1 * e2) * e3  ("Associativity of *")
        case Op(o, e1, Op(p, e2, e3)) if o == p:
            return Op(o, Op(p, e1, e2), e3)

        # Optimize sub-expressions.
        case Op(o, e1, e2):
            e1_opt = optimize_step(e1)
            if e1_opt is not None:
                return Op(o, e1_opt, e2)
            e2_opt = optimize_step(e2)
            if e2_opt is not None:
                return Op(o, e1, e2_opt)
            return None

        case _:
            return None


def optimize_step_if(e: Node) -> Optional[Node]:
    # Evaluation of constants ("Constant Folding")
    if type(e) is Op and e.sym == OpSym.ADD and type(e.left) is Val and type(e.right) is Val:
        return Val(e.left.value + e.right.value)
    elif type(e) is Op and e.sym == OpSym.MUL and type(e.left) is Val and type(e.right) is Val:
        return Val(e.left.value * e.right.value)

    # e + e  →  2 * e  ("Common sub-expression elimination")
    elif type(e) is Op and e.sym == OpSym.ADD and e.left == e.right:
        return Op(OpSym.MUL, Val(2), e.left)

    # e1 + (e2 + e3)  →  (e1 + e2) + e3  ("Associativity of +")
    # e1 * (e2 * e3)  →  (e1 * e2) * e3  ("Associativity of *")
    elif type(e) is Op and type(e.right) is Op and e.sym == e.right.sym:
        return Op(e.sym, Op(e.right.sym, e.left, e.right.left), e.right.right)

    # Optimize sub-expressions.
    elif type(e) is Op:
        e1_opt = optimize_step(e.left)
        if e1_opt is not None:
            return Op(e.sym, e1_opt, e.right)
        e2_opt = optimize_step(e.right)
        if e2_opt is not None:
            return Op(e.sym, e.left, e2_opt)
        return None

    else:
        return None


def optimize(e: Node) -> list[Node]:
    es: list[Node] = []
    e2: Optional[Node] = e
    while e2 is not None:
        es.append(e2)
        e2 = optimize_step(e2)
    return es


if __name__ == '__main__':
    while True:
        s = input("> ")
        if s in ["q", "quit"]:
            print("Good bye!")
            break
        e = parse(s)
        if e is None:
            print("Invalid input.")
        else:
            for e2 in optimize(e):
                print("= " + node_to_str(e2))
        print()
