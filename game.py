import random

def valid_the_guess(player_guess, strng_of_right_or_wrong_guesses):
    if len(player_guess) != 1 or not(('a' <= player_guess <= 'z' or 'A' <= player_guess <= 'Z')):
        print()
        print("Illegal input. choise again.")
        return False
    if player_guess in strng_of_right_or_wrong_guesses:
        print()
        print("You almost guess it")
        return False
    return True

def print_the_right_guesses_and_amount_mistakes(list_of_right_guesses, amount_of_mistakes):
    print()
    for i in range(len(list_of_right_guesses)):
        print(list_of_right_guesses[i], end="")
    print()
    print("You have", amount_of_mistakes, "more mistakes")
    print("Enter a guess: ", end="")

def check_if_right_guess(player_guess, cur_word, list_of_right_guesses, amount_of_mistakes):
    if player_guess in cur_word:
        for i in range(len(cur_word)):
            if cur_word[i] == player_guess:
                list_of_right_guesses[i] = player_guess
    else:
        amount_of_mistakes -= 1
    if '_' not in list_of_right_guesses:
        amount_of_mistakes = 0

    return amount_of_mistakes


def print_win_or_loose(cur_word, list_of_right_guesses):
    print(cur_word)
    if '_' in list_of_right_guesses:
        print("You loose")
    else:
        print("You won!")

def main():

    words_list = ['dad', 'ariel', 'hi']
    amount_of_mistakes = 3
    cur_word = random.choice(words_list)
    list_of_right_guesses = []
    strng_of_right_or_wrong_guesses = ""

    for i in range(len(cur_word)):
        list_of_right_guesses.append('_')


    while amount_of_mistakes > 0:
        print_the_right_guesses_and_amount_mistakes(list_of_right_guesses, amount_of_mistakes)

        player_guess = input()

        if valid_the_guess(player_guess, strng_of_right_or_wrong_guesses) == False:
            continue
        
        strng_of_right_or_wrong_guesses += player_guess

        amount_of_mistakes = check_if_right_guess(player_guess, cur_word, list_of_right_guesses, amount_of_mistakes)


    print_win_or_loose(cur_word, list_of_right_guesses) 

 
if __name__ == '__main__':
    main()


