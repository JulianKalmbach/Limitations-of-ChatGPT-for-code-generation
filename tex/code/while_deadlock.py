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
