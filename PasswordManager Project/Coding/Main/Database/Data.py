from dataclasses import dataclass

from functools import cache

from time import sleep

import sys

import os


version = f'Beta 1.5.16'     # *Semantic Numbering.

Users_Info = {
    "Users" : {}
}

Operations = {  1 : "Viewing Passwords"
              , 2 : "Adding Password" 
              , 3 : "Removing Password" 
              , 4 : "Changing MasterPassword"
              , 5 : "ForGot MasterPassword"
              , 6 : "Quit"}

user_management_operations = {
      7 : "Change User"
    , 8 : "Add User" 
    , 9 : "Delete user"
}

# Usage in different Input accepting , Denying.
allowed_character = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ,"0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , ]
UpperCase_Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ,]
LowerCase_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]

QUIT_LETTERCASE = [
    "QUIT",
    "Quit",
    "quit",
    "QuIt",
    "quIT",
    "QUit",
    "qUIT",
    "qUIt",
    "QuIt",
    "QuiT",
    "QuIt",
    "qUIT",
    "QUIT",
    "qUiT",
    "quIt",
    "QUiT",
    "QUiT",
    "QuIt",
    "QUiT",
    "quiT",
    "quIt"
]

TABS = "\t"

# ANSI COLORING.
color_red = "\33[31m"
color_blue = "\33[34m"
bold = "\33[1m" 
format_reversed = "\33[7m"
format_reset = "\33[0m"


def clean() -> None:
    """Clear the terminal"""

    os.system('cls')


def loading():
    print(F"{color_blue}Loading{color_red} Assets....")
    sleep(1)
    clean()
    print(F"{color_blue}Loading{color_red} Assets...")
    sleep(1)
    clean()
    print(F"{color_blue}Loading{color_red} Assets..")
    sleep(1)
    clean()
    print(F"{color_blue}Loading{color_red} Attachments....")
    sleep(1)
    clean()
    print(F"{color_blue}Loading{color_red} Attachments...")
    sleep(1)
    clean()
    print(F"{color_blue}Loading{color_red} Attachments..")
    sleep(1)
    clean()
    print(F"{color_blue}Loading{color_red} Attachments.")
    sleep(1)
    clean()
    print(F"{color_red}Loading{color_blue} Done.")
    sleep(1)


    clean()


def termination():
            """Exit the program with goodbye message."""

            clean()
            print("\33[ Thanks for Using KhodeDan's Password Manager.")
            sleep(4)
            clean()
            print("\33[1;31;40mQuitting.... \33[0m")
            sleep(3)
            clean()

            sys.exit()   


def isusername(UserName : str):

    UserName_Last_Limit = 13     
    UserName_First_limit = 3     
    UserName_Lengh = len(UserName)   


    if UserName_First_limit > UserName_Lengh :
        return False

    
    if UserName_Last_Limit < UserName_Lengh:
        return False
    

    if UserName.isdigit():
        return False

    
    for character in UserName:

        if character not in allowed_character:
        
            return False
    
    return True


def isbirthyear(birthyear : int):
    
    Age_First_Limit = 1923
    Age_Last_Limit = 2022


    try:
        if birthyear > Age_Last_Limit:
            return False
        

        if birthyear < Age_First_Limit:
            return False
        

        return True
    
    except:
        return False


def isbirthmonth(birthmonth : int):

    birthmonth_First_Limit = 1
    birthmonth_Last_Limit = 12


    if birthmonth > birthmonth_Last_Limit:
        return False
    
    if birthmonth < birthmonth_First_Limit:
        return False
    

    return True


def isbirthday(birthday : int):

    try:

        Birthday_First_limit = 1
        Birthday_Last_limit = 31


        if birthday > Birthday_Last_limit:
            return False
        
        if birthday < Birthday_First_limit :
            return False
        

        return True
    
    except:
        
        return False



def ismasterpassword(MasterPassword : str):

    point = 3
    MasterPasswordFirstLimit = 5
    MasterPasswordLastLimit = 15
    HasNumber = False
    HasUpperCase = False
    HasLowerCase = False
    MasterPasswordLengh = len(MasterPassword)


    for character in MasterPassword:
        
        if character in Numbers:
            HasNumber = True
            point = point - 1

        elif character in UpperCase_Letters:
            HasUpperCase = True
            point = point - 1
        
        elif character in LowerCase_Letters:
            HasLowerCase = True
            point = point - 1


    if point + MasterPasswordLengh == 3 and MasterPasswordLengh > MasterPasswordFirstLimit and MasterPasswordLengh < MasterPasswordLastLimit and HasNumber == True and HasLowerCase == True and HasUpperCase == True:
        return True
    

    else:
        return False


def ispassword(password):

    Password_Firstlimi = 1   # Define a variable with the value of int 1 , Which will act as the limitation for the user entry lengh.
    Password_Lastlimit = 30  # Define a variable with the value of int 50 , Which will act as the limitation for the user entry lengh.
    Password_Lengh = len(password)   # Define a variable which will keep the lengh of the entered password , As value.



    if Password_Lengh > Password_Lastlimit:
        return False
    

    if Password_Lengh < Password_Firstlimi:
        return False
    

    return True


def equality_check(string : str , MasterPassword : str) -> bool:


    if string == MasterPassword:


        return True
    

    return False


def get_key_by_value(dictionary : dict , value):
    """return the key of dictionary by providing its value"""
    
    for key,value in dictionary.items():
        
        if key == value:
            return key


def is_yes_no(data) -> bool:

    if not data == "yes" or "no":
        return False
    
    return True

 
@dataclass
class birthDateDatabase:
    """The whole birthday calculation databse ( Keeps all the variables )"""

    birthdate_add_pass : str = None
    birth_day : str = None
    birth_month : str = None
    birth_year : str = None
    full_birthday : str = None

    add_pass_answer : bool = False
    confirm_birthday : str = None
    confirm_birthmonth : str = None
    confirm_birthyear : str = None
    confirm_full_birthdate : str = None

    LOOP1 : bool = True
    LOOP2 : bool = True
    LOOOP3 : bool = True
    LOOP4 : bool = True
    LOOP5 : bool = True

    invalid_entry : bool = False
    

class birthDateFunctions:

    @staticmethod
    def add_pass() -> bool:
        """Ask the User if they want to add their birthday"""

        while birthDateDatabase.LOOP1 :

            # RESETTING THE ENTRY CORRECTION.
            birthDateDatabase.invalid_entry = False
            clean()

            birthDateDatabase.birthdate_add_pass = input(
                f"{color_blue} Would you like to add A birthday to your account ?(Answer with yes or no only) : ")
            birthDateDatabase.birthdate_add_pass = birthDateDatabase.birthdate_add_pass.lower()

            if not is_yes_no(birthDateDatabase.birthdate_add_pass):

                clean()
                print(f"{color_red} That Is not a yes or no , Please try again{color_blue}.")
                sleep(4)
                birthDateDatabase.invalid_entry = True
                continue
            
            if birthDateDatabase.birthdate_add_pass == "no":

                clean()
                print(f"{color_red} Diverting to the main menu.")
                sleep(4)
                clean()
                birthDateDatabase.add_pass_answer = False
                birthDateDatabase.LOOP1 = False
                continue
            
            clean()
            

    @staticmethod
    def calculation() -> None:
        """Calculate the full birthdate of the user"""

        birthDateDatabase.full_birthday = f"{birthDateDatabase.birth_day}/{birthDateDatabase.birth_month}\
            /{birthDateDatabase.birth_year}"
        
        return birthDateDatabase.full_birthday
    
birthDateFunctions.add_pass()