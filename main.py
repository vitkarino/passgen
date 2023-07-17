import string
import csv
import random
import time
import os

class bcolors:
    OKGREEN = '\033[92m'
    PROMPT = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    DEFAULT = '\033[96m'
    

def prnt(msg, type):
    if type == "error":
        print(bcolors.FAIL + msg + bcolors.ENDC)
    elif type == "success":
        print(bcolors.OKGREEN + msg + bcolors.ENDC)
    else:
        print(bcolors.DEFAULT + msg + bcolors.ENDC)


def inpt(msg, type):
    if type == "prompt":
        return input(bcolors.PROMPT + msg + bcolors.ENDC)
    else:
        return ""

def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('clear')


def generate():
    clear_console()

    length = 0
    
    while length < 1:
        length = inpt("Enter length of password: ", "prompt")
        
        try:
            length = int(length)
            if length < 1:
                prnt("Error! Length must be a positive number.", "error")
            else:
                break
        except ValueError:
            prnt("\nError! Length must be a number.", "error")

    prnt("\nGenerating password...", "default")
    time.sleep(1)
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all_chars = lower + upper + num
    password = "".join(random.choices(all_chars, k=length))
    prnt("\nGenerated password: " + password, "default")

    option = ""
    while option not in ['y', 'n']:
        option = inpt("\nWould you like to save this password? (y/n): ", "prompt")
        if option == "y":
            name = inpt("\nEnter name for password: ", "prompt")
            save_password(name, password)
        elif option == "n":
            menu()
        else:
            prnt("\nError! Invalid option.", "error")


def save_password(name, password):
    with open("passwords.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, password])

    prnt("\nPassword saved successfully!", "success")
    time.sleep(3)
    menu()


def saved_passwords():
    clear_console()

    if os.stat("passwords.csv").st_size == 0:
        prnt("No passwords saved.", "default")
    else:
        prnt("Saved passwords:\n", "default")
    
    with open("passwords.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0] + ": " + row[1])
    
    inpt("\nPress enter to return to menu...", "prompt")
    menu()


def clear_passwords():
    clear_console()

    option = ""
    while option not in ['y', 'n']:
        option = inpt("Are you sure you want to clear all saved passwords? This cannot be undone (y/n): ", "prompt")
        if option == "y":
            with open("passwords.csv", "w") as file:
                writer = csv.writer(file)
            break
        elif option == "n":
            menu()
        else:
            prnt("\nError! Invalid option.\n", "error")
    
    menu()
def menu():
    clear_console()

    prnt(
"""Welcome! Please choose an option:\n
1. Generate new password
2. View saved passwords
3. Clear saved passwords
4. Exit""", "default"
    )

    option = ""

    while option not in ['1', '2', '3', '4']:
        option = inpt("\nEnter option: ", "prompt")
        if option == "4":
            prnt("\nThanks for using my app!\nHave a nice day!", "success")
            time.sleep(3)
            break
        if option == "3":
            clear_passwords() 
            break
        if option == "2":
            saved_passwords()  
            break
        if option == "1":
            generate()  
            break
        else:
            prnt("\nError! Invalid option.", "error")


menu()
