from dataclasses import dataclass , fields

from time import sleep

import sys

import os


current_version = f'1.8.25'

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

# Usage in different Input accepting and Denying.
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

color_red = "\33[31m"
color_blue = "\33[34m"
bold = "\33[1m" 
format_reversed = "\33[7m"
format_reset = "\33[0m"


def quit() -> None:
    """Terminate a function or the main program"""
    sys.exit()


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


def good_bye():
            """Exit the program with goodbye message."""

            clean()
            print("\33[ Thanks for Using KhodeDan's Password Manager.")
            sleep(4)
            clean()
            print("\33[1;31;40mQuitting.... \33[0m")
            sleep(3)
            clean()

            quit()


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



    if birthyear > Age_Last_Limit:
        return False
        

    if birthyear < Age_First_Limit:
        return False
        

    return True
    

def is_birth_month(birthmonth : int):

    birthmonth_First_Limit = 1
    birthmonth_Last_Limit = 12



    if birthmonth > birthmonth_Last_Limit:
        return False
        
    if birthmonth < birthmonth_First_Limit:
        return False
    
    return True
    

def is_birth_day(birthday : int):

    Birthday_First_limit = 1
    Birthday_Last_limit = 31


    if birthday > Birthday_Last_limit:
        return False
        
    if birthday < Birthday_First_limit :
        return False
        

    return True
    

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

    password_character_limit = 1   
    password_ending_character_limit = 30 
    Password_Lengh = len(password)   

    if Password_Lengh > password_ending_character_limit:
        return False
    
    if Password_Lengh < password_character_limit:
        return False
    
    return True


def equality_check(arg1 : str , arg2 : str) -> bool:
    """Checks if two strings are equal to each other"""

    if arg1 == arg2:
        return True

    return False


def get_key_by_value(dictionary : dict , value):
    """return the key of dictionary by providing its value"""
    
    for key,value in dictionary.items():
        
        if key == value:
            return key


def is_yes_or_no(user_input) -> bool:

    if not user_input.lower() == "yes" and not user_input.lower() == "no":
        return False
    
    return True

 
@dataclass
class BirthDateDatabase:
    """Database of the collect_birthdate function Operation (Keeps all the variables.)"""

    birthdate_add_or_pass_input : str = None
    birth_day_input :int = None
    birth_month_input : int = None
    birth_year_input : int = None
    confirm_full_birth_date_input : str = None

    accept_to_add_birthdate : bool = False
    added_birthday : bool = False
    added_birthmonth : bool = False
    added_birthyear : bool = False
    confirmed_full_birthdate : bool = False

    add_or_pass_invalid_entry : bool = False
    input_birth_day_invalid_entry : bool = False
    input_birth_month_invalid_entry : bool = False
    input_birth_year_invalid_entry : bool = False
    confirm_full_birthdate_invalid_entry : bool = False

    full_birth_date : str = None
    
    
class BirthDateFunctions:


    @staticmethod
    def add_or_pass_birthdate() -> bool:
        """Ask the User if they want to add their birthday"""

        clean()
        BirthDateDatabase.birthdate_add_or_pass_input = input(f"{color_blue} Would you like to add A birthday to your account ?({color_red}Answer with yes or no only{color_blue}) : ")
        
        if not is_yes_or_no(BirthDateDatabase.birthdate_add_or_pass_input):
            BirthDateDatabase.add_or_pass_invalid_entry = True
            return None
        
        if BirthDateDatabase.birthdate_add_or_pass_input.lower() == "no":
            BirthDateDatabase.accept_to_add_birthdate = False
            return None
        
        BirthDateDatabase.accept_to_add_birthdate = True
    

    @staticmethod
    def input_birthday() -> bool:
        """Takes the user birthday"""

        clean()

        BirthDateDatabase.birth_day_input = input(f"Please enter the day you were born({color_red}1 to 31{color_blue}) : ")

        if not BirthDateDatabase.birth_day_input.isdigit():
            BirthDateDatabase.input_birth_day_invalid_entry = True
            return None
        
        BirthDateDatabase.birth_day_input = int(BirthDateDatabase.birth_day_input)

        if not is_birth_day(BirthDateDatabase.birth_day_input):
            BirthDateDatabase.input_birth_day_invalid_entry = True
            return None
        
        BirthDateDatabase.added_birthday = True
    

    @staticmethod
    def input_birthmonth() -> bool:
        """Takes the user birthmonth"""

        clean()
        BirthDateDatabase.birth_month_input = input(f"Please enter the month you were born({color_red}1 to 12{color_blue}) : ")

        if not BirthDateDatabase.birth_month_input.isdigit():
            BirthDateDatabase.input_birth_month_invalid_entry = True
            return None
        

        BirthDateDatabase.birth_month_input = int(BirthDateDatabase.birth_month_input)
        

        if not is_birth_month(BirthDateDatabase.birth_month_input):
            BirthDateDatabase.input_birth_month_invalid_entry = True
            return None
        
        BirthDateDatabase.added_birthmonth = True

    
    @staticmethod
    def input_birthyear() -> bool :
        """Takes the user birthyear"""

        clean()
        BirthDateDatabase.birth_year_input = input(f"Please enter the year you were born({color_red}1923 to 202{color_blue}) : ")

        if not BirthDateDatabase.birth_year_input.isdigit():
            BirthDateDatabase.input_birth_year_invalid_entry = True
            return None
        

        BirthDateDatabase.birth_year_input = int(BirthDateDatabase.birth_year_input)
        

        if not isbirthyear(BirthDateDatabase.birth_year_input):
            BirthDateDatabase.input_birth_year_invalid_entry = True
            return None
        
        BirthDateDatabase.added_birthyear = True


    @staticmethod
    def calculate_full_birthdate() -> str:
        """Calculate the full birthdate of the user"""

        BirthDateDatabase.full_birth_date = f"\
    {BirthDateDatabase.birth_day_input}/{BirthDateDatabase.birth_month_input}/{BirthDateDatabase.birth_year_input}"
        
        
    @staticmethod
    def confirm_birthdate() -> bool :
        """Ask the user if they confirm the birthdate they inputted."""

        clean()
        BirthDateDatabase.confirm_full_birth_date_input = input(
f"Do you accept {color_red}{BirthDateDatabase.full_birth_date}{color_blue}\
As your birthdate ?\({color_red}Answer with yes or no only{color_blue}) : "
)

        if not is_yes_or_no(BirthDateDatabase.confirm_full_birth_date_input):
            BirthDateDatabase.confirm_full_birthdate_invalid_entry = True
            return None
        
        if BirthDateDatabase.confirm_full_birth_date_input.lower() == "no":
            BirthDateDatabase.confirmed_full_birthdate = False
            return None
        
        BirthDateDatabase.confirmed_full_birthdate = True


BirthDateFunctions.add_or_pass_birthdate()
BirthDateFunctions.input_birthday()
BirthDateFunctions.input_birthmonth()
BirthDateFunctions.input_birthyear()
BirthDateFunctions.calculate_full_birthdate()
BirthDateFunctions.confirm_birthdate()

for field in fields(BirthDateDatabase):
    print(field.name , getattr(BirthDateDatabase, field.name))