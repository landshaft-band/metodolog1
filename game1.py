import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_two(x, y):
    return x * y // gcd(x, y)

def lcm(a, b, c):
    return lcm_two(lcm_two(a, b), c)

def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    for _ in range(3):  # Три раунда
        nums = [random.randint(1, 100) for _ in range(3)]
        correct_answer = lcm(*nums)
        print(f"Question: {nums[0]} {nums[1]} {nums[2]}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer :(, Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    play_game()
