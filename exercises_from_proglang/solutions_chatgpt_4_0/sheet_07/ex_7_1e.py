from exercises_from_proglang.solutions_chatgpt_4_0.sheet_07.ex_7_1c import optimize_step
from exercises_from_proglang.solutions_chatgpt_4_0.sheet_07.tree import Node

def optimize(e: Node) -> list:
    results = [e]
    while True:
        optimized = optimize_step(e)
        if optimized is None:
            break
        results.append(optimized)
        e = optimized
    return results