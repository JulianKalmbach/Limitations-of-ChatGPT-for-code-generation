def reverse(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Testen der Funktion
assert reverse([]) == []
assert reverse([1, 2, 3]) == [3, 2, 1]
assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
print("Alle Tests erfolgreich durchgeführt!")