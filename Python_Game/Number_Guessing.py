'''Number Guessing Game'''

import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("There is currently no higher score, It's you takeing first time...!")
    else:
        print(f'The current high score is'
              f' {min(attempts_list)} attempts')

def start_game():
    attempts = 0
    rand_num = random.randint(1,10)
    print("Hi..! Welcome to the game of guessing...!!")
    player_name = input("What is your name ?\n")
    wanna_play = input(
        f'Hi, {player_name}, would you like to play '
        f'the guessing game? (Enter Yes/No): ')

    if wanna_play.lower() != "yes":
        print("That\'s cool, Thanks..!")
        exit()
    else:
        show_score()
    
    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Chose a number between 1 to 10: "))
            if guess < 1 or guess > 10:
                raise ValueError("please guess a number within the given range.")
            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print("Good..! You Got it...!")
                print(f'It took you {attempts} attempts')
                wanna_play = input("Would you like to play again ? (Enter Yes/No)")
                if wanna_play.lower() != "yes":
                    print("That\'s cool, have a good one...!")
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1,10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print("Chose lower number.")
                elif guess < rand_num:
                    print("Chose higher number.")
        except ValueError as err:
            print("Invalid input... Try again.....")
            print(err)

if __name__ == "__main__":
    start_game()



