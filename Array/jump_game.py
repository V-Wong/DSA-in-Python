import math


def dp_solution(nums):
    def helper(index, nums, seenSteps):
        if index >= len(nums) - 1:
            return True
        elif index + nums[index] <= seenSteps["max"]:
            return False
        elif nums[index] == 0:
            return False
        elif index in seenSteps:
            return seenSteps[index]
        else:
            maxStep = max(nums[index: index + nums[index]])
            for i in range(maxStep, 0, -1):
                res = helper(index + i, nums, seenSteps)
                seenSteps[index + i] = res
                
                if index + i > seenSteps["max"]:
                    seenSteps["max"] = index + i
                
                if res:
                    return True

    return helper(0, nums, {"max": -math.inf})


def iterative_solution(nums):
    furthest_reached = 0
    i = 0

    while i <= furthest_reached and furthest_reached < len(nums):
        furthest_reached = max(furthest_reached, i + nums[i])
        i += 1

    return furthest_reached >= len(nums) - 1


if __name__ == "__main__":
    test_cases = [
        [2, 3, 1, 1, 4],
        [3, 2, 0, 0, 2, 0, 1]
    ]

    for test_case in test_cases:
        print(test_case)
        print(f"Has solution? {iterative_solution(test_case)}")
