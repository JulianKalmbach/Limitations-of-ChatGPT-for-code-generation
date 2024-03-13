from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.ex_7_1c import optimize_step #this was added manually, not by chatgpt
from typing import List
from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.parser import parse
from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.tree import Node


def optimize(e: Node) -> List[Node]:
    results = [e]
    while True:
        next_e = optimize_step(results[-1])
        if next_e is None or next_e == results[-1]:
            break
        results.append(next_e)
    return results


# Test
assert optimize(parse('(x + x) + (x + x)')) == [
    parse('(x + x) + (x + x)'),
    parse('(2 * (x + x))'),
    parse('(2 * (2 * x))'),
    parse('((2 * 2) * x)'),
    parse('(4 * x)')
]