import tkinter
import random



def characters():
    """:returns The function returns a tuple with all the lists the will be declared in this function.
    The first list(index 0) in the tuple contains the lowercase letters.
    The second list(index 1) in the tuple contains all the uppercase letters.
    The third list(index 2) in the tuple contains digit from 0 to 9.
    The fourth list(index 3) in the tuple contains special characters.
    :rtype tuple
    """
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # All the lowercase letters.
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # All the uppercase letters.
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # All the numbers.
    special_characters = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>''.', '?', '/', '\\']  # Special characters.

    return lowercase_letters, uppercase_letters, digits, special_characters


def is_valid_password(password):
    """
    :param password: str.
    :return: True if the password is valid(contains at least 1 special character, 1 digit, 1 upper case letter and 1 lower case letter), False if not.
    :rtype bool
    """
    characters_for_password = characters()  # This variable contains all the characters
    count_lowercase_letters = 0  # This variable counts how many times lowercase letters appear in password.
    count_uppercase_letters = 0  # This variable counts how many times uppercase letters appear in password.
    count_digits = 0  # This variable counts how many times digits appear in password.
    count_special_characters = 0  # This variable counts how many times special characters appear in password.

    for character in password:
        if character in characters_for_password[0]:  # If the character in the lowercase list
            count_lowercase_letters += 1  # Increasing count_lowercase_letters by 1

        if character in characters_for_password[1]:  # If the character in the uppercase list
            count_uppercase_letters += 1  # Increasing count_uppercase_letters by 1

        if character in characters_for_password[2]:  # If the character in the digits list
            count_digits += 1  # Increasing count_digits by 1

        if character in characters_for_password[3]:  # If the character in the special characters list
            count_special_characters += 1  # Increasing count_special_characters by 1

    if count_lowercase_letters > 0 and count_uppercase_letters > 0 and count_digits > 0 and count_special_characters > 0:  # If there is at least one lowercase letter, one uppercase letter, one digit and one special character it will return True. If not, it will return False.
        return True
    return False

def generate_password(length = 10):
    """
    :param length: int. The length of the password.
    :return Random password. The length of the password will be length.
    :rtype str
    """
    password = str()  # This variable contains the password
    characters_for_password = characters()  # This variable contains all the characters

    if length < 8:  # If length is less than 8
        length = 8  # Set the length of the password to 8

    else:
        for i in range(0, length):  # for loop to generate the password.
            random_number = random.randint(0, len(characters_for_password) - 1)  # Random numbers to select prom which list we take random characters. random_number is the index of the list in characters_for_password from which we will take a random character.
            random_character = random.randint(0, len(characters_for_password[random_number]) - 1)  # Select random index in the random list.

            password += str(characters_for_password[random_number][random_character])  # Adding the match character to the password.

    return password


def enter_password(length = 10):
    """
    This function creates random password. If the password is valid, it will enter the password to the entry. If not, it will generate new passwords until there will be a valid password.
    :param length: int. The length of the password.
    """

    if length < 8:  # If length is less than 8
        length = 8  # Set the length of the password to 8

    password = generate_password(length)

    while not is_valid_password(password):  # While the password is invalid.
        password = generate_password(length)  # Generates new password

    return password


def main():

    def button_click(number):
        """This function shows the numbers on entry"""
        current = entry.get()
        entry.delete(0, tkinter.END)
        entry.insert(0, str(current) + str(number))  # Inserts the number to the Entry.


    def button_end_action():
        """End action.
        This function checks if the player pressed the minus button.
        If so, it will delete everything in entry and will show the password."""
        number = entry.get()
        number = int(number)

        entry.delete(0, tkinter.END)
        entry.insert(0, f"Your password is: {enter_password(number)}")  # Shows the password on the screen.


    root = tkinter.Tk()  # Root
    root.title("Random Password Generator")

    label = tkinter.Label(root, text = "Please enter the length of the password.\nPress the - button to get your random password")
    label.grid(row = 0, column = 1)  # Set label in root.

    entry = tkinter.Entry(root, width = 90)  # We will display the password in entry.
    entry.grid(row = 1, column = 1, padx = 10, pady = 10)  # Set entry in root.

    # Create buttons.
    button0 = tkinter.Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
    button1 = tkinter.Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
    button2 = tkinter.Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
    button3 = tkinter.Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
    button4 = tkinter.Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
    button5 = tkinter.Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
    button6 = tkinter.Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
    button7 = tkinter.Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
    button8 = tkinter.Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
    button9 = tkinter.Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))

    button_end = tkinter.Button(root, text = "-", padx = 40, pady = 20, command = button_end_action)
    # Create buttons.

    # Add the buttons on the screen.
    button7.grid(row = 2, column = 0)
    button8.grid(row = 2, column = 1)
    button9.grid(row = 2, column = 2)

    button4.grid(row = 3, column = 0)
    button5.grid(row = 3, column = 1)
    button6.grid(row = 3, column = 2)

    button1.grid(row = 4, column = 0)
    button2.grid(row = 4, column = 1)
    button3.grid(row = 4, column = 2)

    button0.grid(row = 5, column = 1)

    button_end.grid(row = 5, column = 2)
    # Add the buttons on the screen.

    root.mainloop()


if __name__ == '__main__':
    main()
