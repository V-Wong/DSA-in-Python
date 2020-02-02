from stack import Stack


def balanced_brackets(string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(string) and is_balanced:
        paren0 = string[index]
        
        if paren0 in "{([":
            s.push(paren0)
        elif paren0 in "])}":
            if s.is_empty():
                is_balanced = False
            else:
                paren1 = s.pop()
                if not matching_brackets(paren0, paren1):
                    is_balanced = False

        index += 1

    return s.is_empty() and is_balanced
    

def matching_brackets(paren0, paren1):
    matching_sets = ["()", "[]", "{}"]

    return paren0 + paren1 in matching_sets or paren1 + paren0 in matching_sets


if __name__ == "__main__":
    test_cases = ["(()))", ")))", "[({})]"]

    for test_case in test_cases:
        print(test_case, balanced_brackets(test_case))