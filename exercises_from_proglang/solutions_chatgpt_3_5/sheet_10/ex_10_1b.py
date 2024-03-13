def compute_grade(student_points, max_points, student_name):
    pass_points = calculate_passing_points(max_points, student_points)
    min_grade_points = max_points // 5
    points = student_points.get(student_name, 0)

    if points < pass_points:
        return 5
    elif points < pass_points + min_grade_points:
        return 4
    elif points < pass_points + 2 * min_grade_points:
        return 3
    elif points < pass_points + 3 * min_grade_points:
        return 2
    else:
        return 1


def calculate_passing_points(max_points, student_points):
    failure_threshold = 0.4
    pass_points = max_points // 2

    # Calculate the number of students who passed
    passed_students = sum(1 for points in student_points.values() if points >= pass_points)
    # Calculate the percentage of students who passed
    pass_rate = passed_students / len(student_points)

    # Adjust pass points until the failure threshold is met
    while pass_rate > 1 - failure_threshold:
        pass_points -= 1
        passed_students = sum(1 for points in student_points.values() if points >= pass_points)
        pass_rate = passed_students / len(student_points)

    return pass_points


# Beispielaufruf
student_points = {"Adam": 63, "John": 112, "Donald": 43}
print(compute_grade(student_points, 120, "Adam"))
