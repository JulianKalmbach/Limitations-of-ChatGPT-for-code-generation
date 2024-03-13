def only_positive(numbers):
    return [num for num in numbers if num > 0]

# Test the function
assert only_positive([]) == []
assert only_positive([1, 2, 3]) == [1, 2, 3]
assert only_positive([-8, 1, -5, -9, 2, -7, 3, -6, 0]) == [1, 2, 3]

"Die Tests waren erfolgreich. Die Funktion `only_positive` funktioniert wie erwartet."