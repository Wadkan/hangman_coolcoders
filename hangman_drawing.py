import os

def draw_screen(hashed_password, used_letters, lives):
    os.system('clear')

    if lives == 0:
        print("     ___")
        print("    /   |" + "   PASSWORD:      " + hashed_password)
        print("   |    O" + "   USED LETTERS:  " + used_letters)
        print("   |   /|\ ")
        print("   |   / \ " + " LIVES: " + str(lives))
        print("___|___")
    elif lives == 1:
        print("     ___")
        print("    /   |" + "   PASSWORD:      " + hashed_password)
        print("   |    O" + "   USED LETTERS:  " + used_letters)
        print("   |   /|\ ")
        print("   |   /" + "    LIVES: " + str(lives))
        print("___|___")

    elif lives == 2:
        print("     ___")
        print("    /   |" + "   PASSWORD:      " + hashed_password)
        print("   |    O" + "   USED LETTERS:  " + used_letters)
        print("   |   /|\ ")
        print("   |" + "        LIVES: " + str(lives))
        print("___|___")

    elif lives == 3:
        print("     ___")
        print("    /   |" + "   PASSWORD:      " + hashed_password)
        print("   |    O" + "   USED LETTERS:  " + used_letters)
        print("   |   /|")
        print("   |" + "        LIVES: " + str(lives))
        print("___|___")

    elif lives == 4:
        print("     ___")
        print("    /   |" + "   PASSWORD:      " + hashed_password)
        print("   |    O" + "   USED LETTERS:  " + used_letters)
        print("   |    |")
        print("   |" + "        LIVES: " + str(lives))
        print("___|___")

    elif lives == 5:
        print("     ___")
        print("    /   |" + "   PASSWORD:      " + hashed_password)
        print("   |    O" + "   USED LETTERS:  " + used_letters)
        print("   |")
        print("   |" + "        LIVES: " + str(lives))
        print("___|___")

    elif lives == 6:
        print("     ___")
        print("    /   |" + "   PASSWORD:      " + hashed_password)
        print("   |" + "        USED LETTERS:  " + used_letters)
        print("   |")
        print("   |" + "        LIVES: " + str(lives))
        print("___|___")

    elif lives == 7:
        print("")
        print("" + "            PASSWORD:      " + hashed_password)
        print("   |" + "        USED LETTERS:  " + used_letters)
        print("   |")
        print("   |" + "        LIVES: " + str(lives))
        print("___|___")

    elif lives == 8:
        print("")
        print("" + "            PASSWORD:      " + hashed_password)
        print("" + "            USED LETTERS:  " + used_letters)
        print("")
        print("" + "            LIVES: " + str(lives))
        print("_______")

    elif lives == 9:
        print("")
        print("" + "            PASSWORD:      " + hashed_password)
        print("" + "            USED LETTERS:  " + used_letters)
        print("")
        print("" + "            LIVES: " + str(lives))
        print("")
