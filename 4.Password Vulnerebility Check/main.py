from time import time, sleep
from sys import argv
from string import ascii_letters, digits, punctuation
from itertools import product
def main():
    password = input("Enter Password: ")
    while password == "":
        print("Please enter a password!")
        password = input("Password: ")
    length = 0
    results = False
    printable = False
    if len(argv) == 2:
        printable = True
    timestart = time()
    while results == False:
        length += 1
        print(f"Trying passwords with the length of {length}")
        results = crackpass(password, length, printable)
    timeend = time()
    elapsed = timeend - timestart
    print(f"Your password was cracked! It took {elapsed} seconds to crack your password. ")


def crackpass(password, length, printable):
    for passcode in product(ascii_letters + digits + punctuation, repeat=length):
        if printable:
            print("".join(passcode))    
        if "".join(passcode) == password:
            return True
    return False        


if __name__ == "__main__":
    main()