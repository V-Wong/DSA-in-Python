def intersection(l0, l1):
    intersection = []

    i = j = 0
    while i < len(l0) and j < len(l0):
        if l0[i] == l1[j]:
            if i == 0 or l0[i] != l0[i - 1]:
                intersection.append(l0[i])
            i += 1
            j += 1
        elif l0[i] < l1[j]:
            i += 1
        else:
            j += 1

    return intersection


if __name__ == "__main__":
    test_cases = [
        [[1, 3, 5], [2, 4, 6]],
        [[1, 1, 1], [1, 1, 1]],
        [[1, 2, 3], [0, 1, 3]]
    ]

    for test_case in test_cases:
        l0, l1 = test_case[0], test_case[1]
        print(intersection(l0, l1))