def reverse(lst):
    """
    Diese Funktion nimmt eine Liste als Argument und gibt eine Liste mit den gleichen Elementen in umgedrehter
    Reihenfolge zurück, ohne die built-in Funktion `reversed` zu verwenden.
    """
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Testen der Funktion
assert reverse([]) == []
assert reverse([1, 2, 3]) == [3, 2, 1]
assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

# Die Tests waren erfolgreich, wenn bis hierhin keine AssertionErrors ausgelöst wurden.
"Alle Tests erfolgreich durchgeführt!"