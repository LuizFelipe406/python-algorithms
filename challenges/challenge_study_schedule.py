def study_schedule(permanence_period, target_time):
    counter = 0
    for student_period in permanence_period:
        try:
            if student_period[0] <= target_time <= student_period[1]:
                counter += 1
        except TypeError:
            return None
    return counter
