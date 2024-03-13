def update_points(student_points, changes):
    max_points = 120

    for name, change in changes.items():
        if name not in student_points:
            raise KeyError(f"{name} wurde nicht gefunden")

        new_points = student_points[name] + change

        if new_points < 0 or new_points > max_points:
            raise ValueError("Die Gesamtpunktzahl muss zwischen 0 und 120 liegen")

        student_points[name] = new_points


# Beispielaufruf
student_points = {"Adam": 63, "John": 112, "Donald": 43}
changes = {"Adam": 3, "John": -7}

try:
    update_points(student_points, changes)
    print(student_points)
except (KeyError, ValueError) as e:
    print(e)
