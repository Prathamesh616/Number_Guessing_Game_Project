import random


game_will_continue = True
while game_will_continue:
    random_number = random.randint(1, 101)
    print(random_number)

    print("Welcome to the Number Guessing Game!!!")
    print("I'm thinking of a number between 1 to 100 for you to guess!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    # print(f"You have {lives} attempt remaining to guess the number.")

    continue1 = True
    while continue1:
        print(f"You have {lives} attempt remaining to guess the number.")
        input_number = int(input("Make a guess:\n"))
        lives = lives - 1
        if input_number > random_number:
            if input_number - 1 == random_number or input_number - 2 == random_number or input_number - 3 == random_number:
                print("You are extremely close on higher side.")
            else:
                print("Too High.")
        elif input_number < random_number:
            if input_number + 1 == random_number or input_number + 2 == random_number or input_number + 3 == random_number:
                print("You are extremely close on lower side.")
            else:
                print("Too Low.")
        else:
            print("You guessed the correct number. Congrats")
            break
        if lives == 0:
            print("All of your lives have ended.")
            continue1 = False

    game_should_continue = input("Do you want to play again. Say 'yes' or 'no'.\n").lower()
    if game_should_continue == "no":
        game_will_continue = False
    print("\n" * 20)

