# Solution exam.py ############################################################

# (a) #########################################################################
def update_points(
        student_points: dict[str, int],
        changes: dict[str, int]):
    for name, additional_points in changes.items():
        if name in student_points:
            new_points = student_points[name] + additional_points
            if new_points > 120 or new_points < 0:
                raise ValueError(
                    "Die Gesamtpunktzahl muss zwischen 0 und 120 liegen")
            student_points[name] = new_points
        else:
            raise KeyError(name + " wurde nicht gefunden")


# (b) #########################################################################
def compute_grade_by_points(
        actual_points: int,
        pass_points: int,
        max_points: int) -> int:
    '''
    Helper: Computing the grade achieved with 'actual_points' under fixed
    'pass_points' and 'max_points'.
    '''
    if actual_points < pass_points:
        return 5

    remaining = actual_points - pass_points
    remaining_max = max_points - pass_points

    if remaining < 0.25 * remaining_max:
        return 4
    elif remaining < 0.5 * remaining_max:
        return 3
    elif remaining < 0.75 * remaining_max:
        return 2
    else:
        return 1


def number_of_fails(
        student_points: dict[str, int],
        pass_points: int) -> int:
    '''Helper: Computes the number of students who failed the exam.'''
    fails = 0

    for points in student_points.values():
        if points < pass_points:
            fails += 1

    return fails


def compute_pass_points(
        student_points: dict[str, int],
        max_points: int) -> int:
    '''
    Helper: Computes 'pass_points' so that at most 40% of the students failed.
    '''
    pass_points = max_points // 2

    while pass_points > 0:
        if number_of_fails(
                student_points, pass_points) / len(student_points) > 0.4:
            pass_points -= 1
        else:
            break

    return pass_points


def compute_grade(
        student_points: dict[str, int],
        max_points: int,
        student_name: str) -> int:
    '''Computes the grade of a student with the name 'student_name'.'''
    pass_points = compute_pass_points(student_points, max_points)

    return compute_grade_by_points(
        student_points[student_name],
        pass_points,
        max_points)


# (c)) ########################################################################
def cluster_by_grade(
        student_points: dict[str, int],
        max_points: int) -> dict[int, str]:
    '''Computes a clustering of the students based on their grades.'''
    d = dict()
    pass_points = compute_pass_points(student_points, max_points)

    for name, points in student_points.items():
        grade = compute_grade_by_points(points, pass_points, max_points)
        if grade in d:
            d[grade].append(name)
        else:
            d[grade] = [name]

    return d
