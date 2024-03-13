# imports were all added manually to fit the data structure
from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.ex_7_1ab import node_to_str
from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.ex_7_1e import optimize
from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.parser import parse

def optimizer_repl():
    print("Optimizer REPL")
    print("Enter an expression or 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input == "quit":
            print("Good bye!")
            break
        expr = parse(user_input)
        if expr is None:
            print("Syntax error.")
            continue
        optimizations = optimize(expr)
        for i, opt_expr in enumerate(optimizations):
            print(f"{node_to_str(opt_expr)}", end="")
            if i < len(optimizations) - 1:
                print(" =", end="")
        print()

# Test the REPL
optimizer_repl()