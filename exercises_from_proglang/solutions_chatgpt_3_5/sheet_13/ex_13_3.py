def lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def parse_csv(lines_gen):
    for line in lines_gen:
        yield line.split(',')

def update_balance(balance, csv_path):
    transactions = parse_csv(lines(csv_path))
    for transaction in transactions:
        amount = float(transaction[2])
        balance += amount
    return balance

update_balance(100.00, "C:/Users/julia/PycharmProjects/Limitations-of-ChatGPT-for-code-generation/exercises_from_proglang/sample_solutions_from_technical_faculty_uni_freiburg/sheet_13/umsatz.csv")