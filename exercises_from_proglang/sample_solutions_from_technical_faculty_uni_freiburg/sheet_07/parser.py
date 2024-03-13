from typing import Optional
from tree import Node, Var, Val, Op, OpSym
from ast import NodeTransformer
import ast


# Python comes with the library `ast` to parse python expressions.
# As our arithmetic language is a subset of python, we first parse them as
# python code and then transform the python tree to a `Node`.


class AstToNode(NodeTransformer):
    def visit_Name(self, node):
        return Var(node.id)

    def visit_Constant(self, node):
        return Val(node.value)

    def visit_Add(self, node):
        return OpSym.ADD

    def visit_Mult(self, node):
        return OpSym.MUL

    def visit_BinOp(self, node):
        op = self.visit(node.op)
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(left, Node) and isinstance(right, Node) and type(op) is OpSym:
            return Op(op, left, right)

    def visit_Expr(self, node):
        return self.visit(node.value)

    def visit_Module(self, node):
        if len(node.body) == 1:
            return self.visit(node.body[0])


def parse(s: str) -> Optional[Node]:
    try:
        n = AstToNode().visit(ast.parse(s))
        if isinstance(n, Node):
            return n
        return None
    except Exception:
        return None
