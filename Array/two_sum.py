def brute_force(array, target):
    for i in range(len(array)):
        for j in range(j + 1, len(array)):
            if array[i] + array[j] == target:
                return [array[i], array[j]]


def hashtable(array, target):
    ht = {}

    for num in array:
        if num in ht:
            return [ht[num], num]
        else:
            ht[target - num] = num


if __name__ == "__main__":
    test_cases = {
        9: [2, 7, 11, 15],
        1: [1],
        2: [1, 3, 1]
    }

    for target, array in test_cases.items():
        print(target, array, hashtable(array, target))