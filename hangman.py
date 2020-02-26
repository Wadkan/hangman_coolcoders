import random

# if used_letters does not exist, and runs on an error, the program declarates it.
try:
    test = used_letters
except NameError:
    used_letters = []


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
            now_used = ""
            break
        else:
            now_used = letter

    if now_used != "":
        for j in used_letters:
            if j != letter:
                now_used = letter
            else:
                print("You've already used this letter.")
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

    return hashed_password == password

# test for is_win function
""" password = "Budapest"
print(is_win("B__", "Budapest"))
"""

def is_loose(life_points):
    '''
    Checks if life points is equal 0

    Args:
    int: The life life_points

    Returns:
    bool: True if life point is equal 0, False otherwise
    '''
    return life_points == 0

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

    guess = input("Try to guess the word! Only one letter, or a whole word.\n")
    guess = guess.lower()
    right_characters = "qwertzuioplkjhgfdsayxcvbnm"
    for check in right_characters:
        if check == guess:
            return True
    print("Wrong. Use only one or more letter(s) Numbers and special chars are prohibited.")
    return False

# test for get_input
# print(get_input())


def main():
    pass

    # used_letters.append(update())
    hashed = ""


    for i in word:
        if i == " ":
            hashed += "  "
        else:
            hashed += "_ "
    return hashed

'''
test for get hashed

if __name__ == '__main__':
    main()
'''