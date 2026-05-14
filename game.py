import random

def valid_the_guess(player_guess, strng_of_right_or_wrong_guesses):
    if len(player_guess) != 1 or not(('a' <= player_guess <= 'z' or 'A' <= player_guess <= 'Z')):
        print()
        print("Illegal input. choise again.")
        return False
    if player_guess in strng_of_right_or_wrong_guesses:
        print()
        print("You already guessed it.")
        return False
    return True


def print_current_state_and_amount_mistakes(list_of_right_guesses, amount_of_mistakes):
    print()
    for i in range(len(list_of_right_guesses)):
        print(list_of_right_guesses[i], end="")
        print(" ", end="")
    print()
    print("You have", amount_of_mistakes, "more mistakes")
    print("Enter a guess: ", end="")


def update_guesses_and_mistakes_state(player_guess, cur_word, list_of_right_guesses, amount_of_mistakes):
    if player_guess in cur_word:
        for i in range(len(cur_word)):
            if cur_word[i] == player_guess:
                list_of_right_guesses[i] = player_guess
    else:
        amount_of_mistakes -= 1
    if '_' not in list_of_right_guesses:
        amount_of_mistakes = 0

    return amount_of_mistakes


def print_win_or_loose(cur_word, list_of_right_guesses):  #print if the player won or lost
    print(cur_word)
    if '_' in list_of_right_guesses:
        print("You lost")
    else:
        print("You won!")


def one_game_procedure(amount_of_mistakes, list_of_right_guesses, strng_of_right_or_wrong_guesses, cur_word):
    while amount_of_mistakes > 0:
            print_current_state_and_amount_mistakes(list_of_right_guesses, amount_of_mistakes)

            player_guess = input()

            if valid_the_guess(player_guess, strng_of_right_or_wrong_guesses) == False:
                continue
            
            player_guess = player_guess.lower()
            strng_of_right_or_wrong_guesses += player_guess

            amount_of_mistakes = update_guesses_and_mistakes_state(player_guess, cur_word, list_of_right_guesses, amount_of_mistakes)


def main():

    WORDS = [
    "apple", "banana", "orange", "grape", "melon",
    "water", "house", "table", "chair", "window",
    "school", "teacher", "student", "pencil", "paper",
    "computer", "keyboard", "mouse", "screen", "phone",
    "music", "guitar", "piano", "drum", "song",
    "river", "ocean", "beach", "mountain", "forest",
    "animal", "tiger", "lion", "zebra", "monkey",
    "rabbit", "horse", "sheep", "goat", "camel",
    "bird", "eagle", "snake", "fish", "shark",
    "pizza", "bread", "cheese", "salad", "soup",
    "coffee", "sugar", "honey", "butter", "cookie",
    "happy", "angry", "funny", "quiet", "brave",
    "smart", "strong", "clean", "dirty", "small",
    "large", "short", "long", "early", "late",
    "green", "yellow", "purple", "black", "white",
    "silver", "gold", "brown", "pink", "blue",
    "summer", "winter", "spring", "autumn", "season",
    "morning", "night", "today", "tomorrow", "yesterday",
    "family", "father", "mother", "brother", "sister",
    "friend", "people", "child", "baby"
]
    want_continue = 'y'

    while want_continue in ('y','Y'):

        amount_of_mistakes = 3
        cur_word = random.choice(WORDS)
        list_of_right_guesses = []
        strng_of_right_or_wrong_guesses = ""

        for i in range(len(cur_word)):
            list_of_right_guesses.append('_')

        one_game_procedure(amount_of_mistakes, list_of_right_guesses, strng_of_right_or_wrong_guesses, cur_word)

        print_win_or_loose(cur_word, list_of_right_guesses) 

        print("Want to play again? (y/n): ")
        want_continue = input()

 
if __name__ == '__main__':
    main()