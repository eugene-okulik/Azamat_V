def guessing_game():
    number = 15
    while True:
        user_input = input("Enter your number: ")
        try:
            guessed_number = int(user_input)
            if guessed_number == number:
                print("Congratulations! You guessed it!")
                break
            elif guessed_number != number:
                print(f"Wrong number. Enter again: {user_input}")
        except ValueError:
            print("That's not a number. Please enter a number.")


guessing_game()
