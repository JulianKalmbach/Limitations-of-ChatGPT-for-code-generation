from exercises_from_proglang.sample_solutions_from_technical_faculty_uni_freiburg.sheet_10.polynom_test import \
    test_many_cracker_n


def crack_1(f):
    a0 = f(0)  # Direkter Wert von a0
    a1 = f(1) - f(0)  # Differenz gibt a1
    return [a0, a1]


# Für die quadratische Funktion verwenden wir eine Matrixlösung zur Bestimmung der Koeffizienten.
def crack_2(f):
    f0 = f(0)
    f1 = f(1)
    f2 = f(2)

    a0 = f0
    # Differenzmethode
    a1 = f1 - f0
    # Lösen für a2 unter Berücksichtigung der bereits bekannten Werte
    a2 = f2 - 2 * f1 + f0

    return [a0, a1, a2]


# Testen der Funktion crack_2 mit den gegebenen Funktionen
def f20(x):
    return 1 + 2 * x + x * x


def f21(x):
    return -1 - 4 * x + 2 * x * x


def f22(x):
    return (x + 1) * (x - 1)


# Anwenden von crack_2 auf die Beispielfunktionen
crack_2_results = [crack_2(f) for f in [f20, f21, f22]]
crack_2_results


def crack_3(f):
    f0 = f(0)
    f1 = f(1)
    f2 = f(2)
    f3 = f(3)

    a0 = f0
    a1 = f1 - f0 - (f2 - 2 * f1 + f0) - ((f3 - 3 * f2 + 3 * f1 - f0) - 3 * (f2 - 2 * f1 + f0) + 2 * (f1 - f0))
    a2 = (f2 - 2 * f1 + f0) - 2 * (f3 - 3 * f2 + 3 * f1 - f0) + 3 * (f2 - 2 * f1 + f0)
    a3 = (f3 - 3 * f2 + 3 * f1 - f0) - 3 * (f2 - 2 * f1 + f0) + 3 * (f1 - f0)

    return [a0, a1, a2, a3]


# Test der Funktion crack_3 mit der gegebenen Funktion
def f30(x):
    return x * (x + 10) * (x - 5)


crack_3_result = crack_3(f30)
crack_3_result
