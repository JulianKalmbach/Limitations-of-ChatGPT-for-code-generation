from exercises_from_proglang.solutions_chatgpt_3_5.sheet_10.ex_10_1b import calculate_passing_points, compute_grade # import added manually


def cluster_by_grade(student_points, max_points):
    pass_points = max_points // 2
    grades = {}

    # Calculate pass points and adjust if necessary
    pass_points = calculate_passing_points(max_points, student_points)

    # Cluster students by grade
    for student, points in student_points.items():
        grade = compute_grade(student_points, max_points, student)
        if grade not in grades:
            grades[grade] = []
        grades[grade].append(student)

    # Remove grades with no students
    grades = {grade: students for grade, students in grades.items() if students}

    return grades

# Beispielaufruf
student_points = {"Mira": 80, "Olivia": 95, "Emily": 83}
print(cluster_by_grade(student_points, 120))
