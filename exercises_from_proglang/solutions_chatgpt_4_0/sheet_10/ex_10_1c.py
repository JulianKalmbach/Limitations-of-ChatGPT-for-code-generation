from exercises_from_proglang.solutions_chatgpt_4_0.sheet_10.ex_10_1b import compute_pass_points, compute_grade # import added manually


def cluster_by_grade(student_points, max_points):
    # Initialisiere das Dictionary, das die Noten als Schlüssel und die Studierendennamen als Werte speichert
    grades_cluster = {}

    # Berechne die Mindestpunktzahl unter Berücksichtigung der Durchfallquote
    pass_points = compute_pass_points(max_points, student_points)

    # Zuordnung der Studierenden zu den Noten
    for student_name, points in student_points.items():
        # Berechne die Note des Studierenden
        grade = compute_grade(student_points, max_points, student_name)

        # Füge den Studierenden der entsprechenden Note hinzu
        if grade not in grades_cluster:
            grades_cluster[grade] = [student_name]
        else:
            grades_cluster[grade].append(student_name)

    return grades_cluster


# Test der Funktion
student_points = {"Mira": 80, "Olivia": 95, "Emily": 83}
clustered_grades = cluster_by_grade(student_points, 120)
clustered_grades
