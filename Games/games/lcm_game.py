import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm_two(x, y):
    return x * y // gcd(x, y)


def lcm(a, b, c):
    return lcm_two(lcm_two(a, b), c)


GAME_RULE = "Find the smallest common multiple of given numbers."


def get_question_and_answer():
    nums = [random.randint(1, 100) for _ in range(3)]
    correct_answer = lcm(*nums)
    question = f"{nums[0]} {nums[1]} {nums[2]}"
    return question, correct_answer
