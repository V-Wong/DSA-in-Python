def optimal_task_assignment(tasks):
    sorted_tasks = sorted(tasks)
    assignments = []

    for i in range(len(tasks) // 2):
        assignments.append((sorted_tasks[i], sorted_tasks[-i - 1]))

    return assignments, max((sum(assignment) for assignment in assignments),
                            default=None)


if __name__ == "__main__":
    test_cases = [
        [1, 3, 1, 2, 3, 4, 9],
        [3, 3, 4, 4, 5, 6],
        [1, 2],
        []
    ]

    for test_case in test_cases:
        print(optimal_task_assignment(test_case))