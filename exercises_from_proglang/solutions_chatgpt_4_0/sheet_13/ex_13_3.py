def lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def parse_csv(lines_generator):
    for line in lines_generator:
        yield line.split(',')

def update_balance(start_balance, csv_path):
    transactions = parse_csv(lines(csv_path))
    next(transactions)  # Überspringt die Kopfzeile
    for date, purpose, amount in transactions:
        start_balance += float(amount)
    return start_balance

# tests manually added
print(update_balance(100.00, "C:/Users/julia/PycharmProjects/Limitations-of-ChatGPT-for-code-generation/exercises_from_proglang/sample_solutions_from_technical_faculty_uni_freiburg/sheet_13/umsatz.csv"))
print(list(parse_csv(["Datum,Verwendungszweck,Betrag","30.12.2020,Bafoeg-Foerdergeld,+514.00"])))