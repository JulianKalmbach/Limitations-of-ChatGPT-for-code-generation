from exercises_from_proglang.solutions_chatgpt_4_0.sheet_07.ex_7_1ab import node_to_str
from exercises_from_proglang.solutions_chatgpt_4_0.sheet_07.ex_7_1e import optimize
from exercises_from_proglang.solutions_chatgpt_4_0.sheet_07.parser import parse


def main():
    while True:
        # Eingabeaufforderung
        input_expr = input("> ")

        # Überprüfung, ob der Benutzer beenden möchte
        if input_expr == "quit":
            print("Good bye!")
            break

        # Versuch, den Eingabestring zu parsen
        parsed_expr = parse(input_expr)
        if parsed_expr is None:
            print("Syntax error.")
            continue

        # Optimierung des Ausdrucksbaums
        optimizations = optimize(parsed_expr)

        # Ausgabe der Optimierungsschritte
        for i, step in enumerate(optimizations):
            if i == 0:
                print(f'= {node_to_str(step)}', end='')
            else:
                print(f'\n= {node_to_str(step)}', end='')
        print('\n')


if __name__ == "__main__":
    main()