from stack import Stack


def decimal_to_binary(num):
    s = Stack()

    while num:
        remainder = num % 2
        num //= 2
        s.push(remainder)

    binary_string = ""
    while not s.is_empty():
        binary_string += str(s.pop())

    return binary_string if binary_string else 0


if __name__ == "__main__":
    test_cases = [0, 1, 2, 4, 8, 16, 12, 31, 413]

    for test_case in test_cases:
        print(test_case, decimal_to_binary(test_case))