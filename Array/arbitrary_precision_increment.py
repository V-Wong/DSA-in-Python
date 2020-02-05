def increment(num_array):
    carry = 0
    
    digit_index = len(num_array) - 1
    while True:
        if num_array[digit_index] + 1 == 10:
            num_array[digit_index] = 0
            carry = 1
        else:
            num_array[digit_index] += 1
            carry = 0

        if digit_index == 0 and carry != 0:
            num_array = [1] + num_array
            break
        elif carry == 0:
            break
        else:
            digit_index -= 1

    return num_array


if __name__ == "__main__":
    test_cases = [
        [1, 1, 1, 1],
        [1, 2, 9, 9],
        [9, 9, 9, 9],
        [0],
        [9, 1, 9]
    ]

    for test_case in test_cases:
        print(f"{test_case} -> {increment(test_case)}")