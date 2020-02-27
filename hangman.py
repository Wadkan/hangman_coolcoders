import random
import os
from hangman_drawing import *


# if used_letters does not exist, and runs on an error, the program declarates it.
# try:
#     test = used_letters
# except NameError:
#     used_letters = []


def pick_capital():
    capitals = ["BUDAPEST", "LONDON", "PARIS", "BERLIN", "ROME", "PRAGUE", "MADRID", "LISBON"]
    random_capital = random.choice(capitals)
    return random_capital.lower()



def get_hashed(word):
    '''
    Generates a password based on the word with dashes instead of letters
    Keeps whitespaces undashed.

    Args:
    str: The word to hash

    Returns:
    str: The hashed password
   '''
    hashed = ""

    for i in word:
        if i == " ":
            hashed += "  "
        else:
            hashed += "_ "
    return hashed

'''
test for get hashed
print(get_hashed("Budapest City"))
'''

def uncover(hashed_password, password, letter):
    '''
    Uncovers all occurences of the given letter in the hashed password based on the password

    Args:
    str: The hashed password
    str: The password
    str: The letter to uncover

    Returns:
    str: The hashed password with uncovered letter
    '''

    global lives
    global correct

    liveplus = 0
    uncover_temp = ""
    ii = -2
    for i in password:
        ii += 2
        if i == letter:
            uncover_temp += letter + " "
            liveplus = 1  # if is 1 will compensate updates decrease
        elif hashed_password[ii] != "_":
            uncover_temp += hashed_password[ii] + " "
        else:
            uncover_temp += "_ "
    if liveplus == 1:
        lives += 1   # just to compensate updates decrease
        correct = 1

    return uncover_temp


# test for uncover
# print(uncover("B u _ _ _ e _ _ ", "Budapest", "t"))



def update(used_letters, letter):
    global lives
    global correct
    now_used = ""

    for i in password:
        if i == letter:
            now_used = letter
            correct = 1
            break
        else:
            now_used = letter
            correct = 0

    if now_used != "":
        for j in used_letters:
            if j != letter:
                now_used = letter
            else:
                print(29 * " " + "!!! YOU'VE ALREADY USED THIS LETTER !!!")
                lives -= 1  # just compensate uncover increase
                now_used = ""
                correct = 0
                break

    if now_used != "":
        lives -= 1   # lose one live
        return now_used + " "
    else:
        return ""



# update function test
# it will update used_letter directly, it has no return value.
# if the letter is equal to one letter from password, it does not update used_letters list and brake.

"""
test for update correction
password = "Budapest"
print(update("abc", "g"))
"""

"""
password = "BUDAPEST"
print(password)

update(used_letters, "r")
print(used_letters)

update(used_letters, "u")
print(used_letters)

update(used_letters, "g")
print(used_letters)
"""


def is_win(hashed_password, password):
    '''
    Checks if the hashed password is fully uncovered

    Args:
    str: The hashed password
    str: The password

    Returns:
    bool:
    '''

    win = "yes"

    for i in hashed_password:
        if i == "_":
            win = "no"

    if win == "yes":
        return True
    else:
        return False

# test for is_win function
""" password = "Budapest"
print(is_win("B__", "Budapest"))
"""

def is_loose():
    '''
    Checks if life points is equal 0

    Args:
    int: The life life_points

    Returns:
    bool: True if life point is equal 0, False otherwise
    '''
    global lives
    return lives == 0

"""
#test for is_loose
life_points = 3
for i in range(4):
    print(i)
    print(life_points)
    print(is_loose(life_points - i))
"""


def get_input():
    '''
    Reads a user input until it contains only letter

    Returns:
    str: The validated input
    '''

    guess = input("Try to guess the word! -> ")
    guess = guess.lower()
    right_characters = "qwertzuioplkjhgfdsayxcvbnm"

    for check in right_characters:
        if check == guess:
            return check
    print(29 * " " + "!!! WRONG CHAR! USE ONLY ONE OR MORE LETTER(s) !!!")

# test for get_input
# print(get_input())


lives = 6
password = ""
hashed_password = ""
used_letters = ""
correct = 0

def main():
    global lives
    global password
    global hashed_password
    global used_letters
    global correct

    used_letters = ""

    run = "yes"
    lives = 9
    password = pick_capital()
    hashed_password = get_hashed(password)
    letter = ""

    correct = 0
    was_wrong = ""

    # print("ps " + password) # this is the password to chet and test :)

    while run == "yes":
        if correct == 0:
            was_wrong = " was wrong."
        else:
            was_wrong = " was correct!"

        # here: put the DRAWING -> drawing(lives, hashed_password, used_letters)
        os.system('clear')
        draw_screen(hashed_password, used_letters, lives)    # drawing

        # old print("PASSWORD:     " + hashed_password + " LIVES: " + str(lives) + "  USED LETTERS: " + used_letters)
        letter = str(get_input())

        hashed_password = uncover(hashed_password, password, letter)
        used_letters += update(used_letters, letter)

        if is_win(hashed_password, password) == True:
            width = int((26 - len(hashed_password)) // 2)
            print(26 * "-" + "\n----You are the winner!---\n" + 26 * "-")
            print(width * "-" + hashed_password.upper() + width * "-" + "\n--------------------------")
            run = "no"
        elif is_loose() == True:
            run = "no"
            width = int(26 - len(password)) // 2
            print(26 * "-" + "\n" + "------> You loose! <------\n------ The word was: -----")
            print(width * "-" + password.upper() + width * "-" + "\n" + 26 * "-")

    if "y" == input(26 * "-" + "\n-> Wanna another game? <-\n" + 26 *"-" + "\ny / n: "):
        main()
    else:
        print(60 * "-" + "\n--- Thank you for choosing Coolcoder's original game! :) ---\n" + 60 * "-")

# more capitals
# welcome screen
# screenplay

if __name__ == '__main__':
    main()
