def compute_pass_points(max_points, student_points):
    # Grundlegende Berechnung der Mindestpunktzahl
    pass_points = max_points // 2

    # Berechne die Durchfallquote
    num_students = len(student_points)
    failed_students = sum(1 for points in student_points.values() if points < pass_points)
    fail_rate = failed_students / num_students

    # Anpassen der Mindestpunktzahl, um die Durchfallquote unter 40% zu halten
    while fail_rate > 0.4 and pass_points > 0:
        pass_points -= 1
        failed_students = sum(1 for points in student_points.values() if points < pass_points)
        fail_rate = failed_students / num_students

    return pass_points


def compute_grade(student_points, max_points, student_name):
    # Berechne die Mindestpunktzahl unter Berücksichtigung der Durchfallquote
    pass_points = compute_pass_points(max_points, student_points)

    # Hole die Punkte für den gegebenen Studierenden
    student_score = student_points.get(student_name)
    if student_score is None:
        raise KeyError(f"{student_name} wurde nicht gefunden")

    # Prüfe, ob der Studierende bestanden hat
    if student_score < pass_points:
        return 5  # Nicht bestanden

    # Berechne die Note basierend auf der Verteilung der Punkte
    score_range = max_points - pass_points
    score_percent = (student_score - pass_points) / score_range

    if score_percent < 0.25:
        return 4
    elif score_percent < 0.5:
        return 3
    elif score_percent < 0.75:
        return 2
    else:
        return 1


# Test der Funktion
student_points = {"Adam": 63, "John": 112, "Donald": 43}
grade = compute_grade(student_points, 120, "Adam")
grade
