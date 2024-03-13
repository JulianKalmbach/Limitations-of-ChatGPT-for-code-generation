def update_points(student_points, changes):
    # Überprüfe, ob alle Namen in 'changes' in 'student_points' vorhanden sind
    for name in changes:
        if name not in student_points:
            raise KeyError(f"{name} wurde nicht gefunden")

    # Aktualisiere die Punkte und überprüfe die Grenzen
    for name, change in changes.items():
        new_points = student_points[name] + change
        if new_points < 0 or new_points > 120:
            raise ValueError("Die Gesamtpunktzahl muss zwischen 0 und 120 liegen")
        student_points[name] = new_points


# Test der Funktion
student_points = {"Adam": 63, "John": 112, "Donald": 43}
changes = {"Adam": 3, "John": -7}

# Funktion aufrufen und Ergebnis ausgeben
try:
    update_points(student_points, changes)
    print(student_points)
except Exception as e:
    print(e)
