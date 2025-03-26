def run_game(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.GAME_RULE)

    for _ in range(3):  # Три раунда
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer :(, Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
