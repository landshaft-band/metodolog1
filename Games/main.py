from engine import run_game
from games import lcm_game, progression_game


def main():
    print("Choose a games:")
    print("1. Least Common Multiple (LCM)")
    print("2. Find the missing number in progression")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        run_game(lcm_game)
    elif choice == "2":
        run_game(progression_game)
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
