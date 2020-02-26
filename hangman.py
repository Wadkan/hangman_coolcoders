import random

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

    uncover_temp = ""
    ii = -2
    for i in password:
        ii += 2
        if i == letter:
            uncover_temp += letter + " "
        elif hashed_password[ii] != "_":
            uncover_temp += hashed_password[ii] + " "
        else:
            uncover_temp += "_ "
    return uncover_temp


# test for uncover
# print(uncover("B u _ _ _ e _ _ ", "Budapest", "t"))



def update(used_letters, letter):

    now_used = ""

    for i in password:
        if i == letter:
            now_used = letter
            break
        else:
            now_used = letter

    if now_used != "":
        for j in used_letters:
            if j != letter:
                now_used = letter
            else:
                print("              !!! YOU'VE ALREADY USED THIS LETTER !!!")
                now_used = ""
                break

    if now_used != "":
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

    for i in hashed_password:
        if i == "_":
            return False
    return True

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
    print("              !!! WRONG CHAR! USE ONLY ONE OR MORE LETTER(s) !!!")

# test for get_input
# print(get_input())

def decrease_lives():
    global lives
    lives -= 1


lives = 6
password = ""
hashed_password = ""
used_letters = ""

def main():
    global lives
    global password
    global hashed_password
    global used_letters

    lives = 6
    password = pick_capital()
    hashed_password = get_hashed(password)

    print("ps " + password)

    while is_win or is_loose:
        print("PASSWORD:     " + hashed_password + "  USED LETTERS: " + used_letters + "   LIVES: " + str(lives))
        letter = str(get_input())

        hashed_password = uncover(hashed_password, password, letter)
        used_letters += update(used_letters, letter)

    if is_win:
        print("You are the winner!")
    elif is_loose:
        print("You loose!")


if __name__ == '__main__':
    main()
