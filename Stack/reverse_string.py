from stack import Stack


def reverse_string(string):
    s = Stack()

    for char in string:
        s.push(char)

    new_string = ""
    while not s.is_empty():
        new_string += s.pop()

    return new_string


if __name__ == "__main__":
    test_cases = ["test", 'abcde', "a", ""]

    for test_case in test_cases:
        print(test_case, reverse_string(test_case))