from dataclasses import dataclass
from time import sleep
import platform
import json
import sys
import os

__version__ = "3.23.21"


def load_from_json():
    with open(r"coding/database/users_data.JSON", "r") as users:
        data = json.load(users)

    return data


users_info = load_from_json()


def dump_to_json():
    with open("coding/main/database/users_data.JSON", "w") as users_data:
        json.dump(users_info, users_data, indent=4)


class UserName:
    def __init__(self, inputted_username):
        self.inputted_username = inputted_username


operations = {
    1: "Viewing Passwords",
    2: "Adding Password",
    3: "Removing Password",
    4: "Changing MasterPassword",
    5: "ForGot MasterPassword",
    6: "Quit",
}

user_management_operations = {7: "Change User", 8: "Add User", 9: "Delete user"}


allowed_character = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
uppercase_letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
lowercase_letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

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
    "quIt",
]

TABS = "\t"

color_red = "\33[31m"
color_blue = "\33[34m"
bold = "\33[1m"
format_reversed = "\33[7m"
format_reset = "\33[0m"


def clean() -> None:
    """Clear the terminal"""

    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


def loading():
    print(f"{color_blue}Loading{color_red} Assets....")
    sleep(1)
    clean()
    print(f"{color_blue}Loading{color_red} Assets...")
    sleep(1)
    clean()
    print(f"{color_blue}Loading{color_red} Assets..")
    sleep(1)
    clean()
    print(f"{color_blue}Loading{color_red} Attachments....")
    sleep(1)
    clean()
    print(f"{color_blue}Loading{color_red} Attachments...")
    sleep(1)
    clean()
    print(f"{color_blue}Loading{color_red} Attachments..")
    sleep(1)
    clean()
    print(f"{color_blue}Loading{color_red} Attachments.")
    sleep(1)
    clean()
    print(f"{color_red}Loading{color_blue} Done.")
    sleep(1)

    clean()


def good_bye():
    """Exit the program with goodbye message."""

    clean()
    print(f"{color_blue} Thanks for Using NyvoJax Password Manager.")
    sleep(4)
    clean()
    print("\33[1;31;40mQuitting.... \33[0m")
    sleep(3)
    clean()

    sys.exit()


def isusername(UserName: str):
    UserName_Last_Limit = 13
    UserName_First_limit = 3
    UserName_Lengh = len(UserName)

    if UserName_First_limit > UserName_Lengh:
        return False

    if UserName_Last_Limit < UserName_Lengh:
        return False

    if UserName.isdigit():
        return False

    for character in UserName:
        if character not in allowed_character:
            return False

    return True


def isbirthyear(birthyear: int):
    Age_First_Limit = 1923
    Age_Last_Limit = 2022

    if birthyear > Age_Last_Limit:
        return False

    if birthyear < Age_First_Limit:
        return False

    return True


def is_birth_month(birthmonth: int):
    birthmonth_First_Limit = 1
    birthmonth_Last_Limit = 12

    if birthmonth > birthmonth_Last_Limit:
        return False

    if birthmonth < birthmonth_First_Limit:
        return False

    return True


def is_birth_day(birthday: int):
    Birthday_First_limit = 1
    Birthday_Last_limit = 31

    if birthday > Birthday_Last_limit:
        return False

    if birthday < Birthday_First_limit:
        return False

    return True


def ismasterpassword(MasterPassword: str):
    point = 3
    MasterPasswordFirstLimit = 5
    MasterPasswordLastLimit = 15
    HasNumber = False
    HasUpperCase = False
    HasLowerCase = False
    MasterPasswordLenght = len(MasterPassword)

    for character in MasterPassword:
        if character in numbers:
            HasNumber = True
            point = point - 1

        elif character in uppercase_letters:
            HasUpperCase = True
            point = point - 1

        elif character in lowercase_letters:
            HasLowerCase = True
            point = point - 1

    if (
        point + MasterPasswordLenght == 3
        and MasterPasswordLenght > MasterPasswordFirstLimit
        and MasterPasswordLenght < MasterPasswordLastLimit
        and HasNumber == True
        and HasLowerCase == True
        and HasUpperCase == True
    ):
        print(point)
        return True

    else:
        return False


print(ismasterpassword(""))


def ispassword(password):
    password_character_limit = 1
    password_ending_character_limit = 30
    Password_Lengh = len(password)

    if Password_Lengh > password_ending_character_limit:
        return False

    if Password_Lengh < password_character_limit:
        return False

    return True


def equality_check(arg1: str, arg2: str) -> bool:
    """Checks if two strings are equal to each other"""

    if not arg1 == arg2:
        return False

    return True


def get_key_by_value(dictionary: dict, inputted_value):
    """return the key of dictionary by providing its value"""

    for key, value in dictionary.items():
        if value == inputted_value:
            return key


def is_yes_or_no(user_input) -> bool:
    if not user_input.lower() == "yes" and not user_input.lower() == "no":
        return False

    return True


@dataclass
class BirthDateDatabase:
    """Database of the collect_birthdate function Operation (Keeps all the variables.)"""

    birthdate_add_or_pass_input: str = None
    birth_day_input: int = None
    birth_month_input: int = None
    birth_year_input: int = None
    confirm_full_birth_date_input: str = None

    accepted_to_add_birthdate: bool = False
    added_birthday: bool = False
    added_birthmonth: bool = False
    added_birthyear: bool = False
    confirmed_full_birthdate: bool = False

    add_or_pass_invalid_entry: bool = False
    input_birth_day_invalid_entry: bool = False
    input_birth_month_invalid_entry: bool = False
    input_birth_year_invalid_entry: bool = False
    confirm_full_birthdate_invalid_entry: bool = False

    full_birth_date: str = None

    STARTING_LOOP = True
    LOOP2 = True
    LOOP3 = True
    LOOP4 = True
    ENDING_LOOP = True


class BirthDateFunctions:
    @staticmethod
    def reset_all_birth_operation_variables():
        """Reset all the variables inside the BirthDateDatabase class ( Excluding the loops )"""

        all_birthdate_variables = [
            variable
            for variable in dir(BirthDateDatabase)
            if not variable.__contains__("LOOP")
            and not variable.startswith("__")
            and not variable.endswith("__")
        ]

        for variable in all_birthdate_variables:
            setattr(BirthDateDatabase, variable, None)

    @staticmethod
    def restart_birthdate_operation():
        all_birthdate_loops = [
            variable
            for variable in dir(BirthDateDatabase)
            if variable.__contains__("LOOP") and not variable.__contains__("STARTING")
        ]

        for loop_variable in all_birthdate_loops:
            setattr(BirthDateDatabase, loop_variable, False)

    @staticmethod
    def all_loop_values_true():
        all_birthdate_loops = [
            variable
            for variable in dir(BirthDateDatabase)
            if variable.__contains__("LOOP")
        ]

        for loop_variable in all_birthdate_loops:
            setattr(BirthDateDatabase, loop_variable, True)

    @staticmethod
    def all_loop_values_false():
        all_birthdate_loops = [
            variable
            for variable in dir(BirthDateDatabase)
            if variable.startswith("LOOP") or variable.endswith("LOOP")
        ]

        for loop_variable in all_birthdate_loops:
            setattr(BirthDateDatabase, loop_variable, False)

    @staticmethod
    def warning_invalid_entry():
        clean()
        print(f"{color_red} Invalid entry{color_blue}.")
        sleep(4)
        clean()

    @staticmethod
    def warning_diverting_to_main_menu():
        clean()
        print(f"{color_red} Diverting to the main menu{color_blue}...")
        sleep(4)
        clean()

    def warning_birthdate_added_to_account():
        """Brief the user that their birthday have been added to their account."""

        print("Your birthday has been added to your current account.")
        sleep(3)
        BirthDateFunctions.warning_diverting_to_main_menu()

    @staticmethod
    def inform_about_birthday():
        """Inform to the user why The program need their birthdate."""

        clean()
        print(
            f"{color_blue} This Is the part where you can decide to add your {color_red}birthday{color_blue} to your account."
        )
        sleep(4)
        print(
            f"Please note that the birthday Is only used in case you forgot your masterpassword."
        )
        sleep(5)
        clean()

    @staticmethod
    def add_or_pass_birthdate() -> bool:
        """Ask the user if they wish to add their birthday."""

        clean()
        BirthDateDatabase.birthdate_add_or_pass_input = input(
            f"{color_blue} Would you like to add A birthday to your account ?({color_red}Answer with yes or no only{color_blue}) : "
        )

        if not is_yes_or_no(BirthDateDatabase.birthdate_add_or_pass_input):
            BirthDateDatabase.add_or_pass_invalid_entry = True
            return False

        if BirthDateDatabase.birthdate_add_or_pass_input.lower() == "no":
            BirthDateDatabase.accepted_to_add_birthdate = False
            return False

        BirthDateDatabase.accepted_to_add_birthdate = True
        return True

    @staticmethod
    def input_birthday() -> bool:
        """Takes the user birthday"""

        clean()

        BirthDateDatabase.birth_day_input = input(
            f"{color_blue}Please enter the day you were born({color_red}1 to 31{color_blue}) : "
        )

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
        BirthDateDatabase.birth_month_input = input(
            f"Please enter the month you were born({color_red}1 to 12{color_blue}) : "
        )

        if not BirthDateDatabase.birth_month_input.isdigit():
            BirthDateDatabase.input_birth_month_invalid_entry = True
            return None

        BirthDateDatabase.birth_month_input = int(BirthDateDatabase.birth_month_input)

        if not is_birth_month(BirthDateDatabase.birth_month_input):
            BirthDateDatabase.input_birth_month_invalid_entry = True
            return None

        BirthDateDatabase.added_birthmonth = True

    @staticmethod
    def input_birthyear() -> bool:
        """Takes the user birthyear"""

        clean()
        BirthDateDatabase.birth_year_input = input(
            f"Please enter the year you were born({color_red}1923 to 2022{color_blue}) : "
        )

        if not BirthDateDatabase.birth_year_input.isdigit():
            BirthDateDatabase.input_birth_year_invalid_entry = True
            return None

        BirthDateDatabase.birth_year_input = int(BirthDateDatabase.birth_year_input)

        if not isbirthyear(BirthDateDatabase.birth_year_input):
            BirthDateDatabase.input_birth_year_invalid_entry = True
            return None

        BirthDateDatabase.added_birthyear = True

    @staticmethod
    def evaluate_full_birthdate() -> str:
        """Calculate the full birthdate of the user"""

        BirthDateDatabase.full_birth_date = f"\
 {BirthDateDatabase.birth_day_input}/{BirthDateDatabase.birth_month_input}/{BirthDateDatabase.birth_year_input}"

    @staticmethod
    def confirm_birthdate() -> bool:
        """Ask the user if they confirm the birthdate they inputted."""

        clean()
        BirthDateDatabase.confirm_full_birth_date_input = input(
            f"Do you accept{color_red}{BirthDateDatabase.full_birth_date}{color_blue} As your birthdate ? \
({color_red}Answer with yes or no only{color_blue}) : "
        )

        if not is_yes_or_no(BirthDateDatabase.confirm_full_birth_date_input):
            BirthDateDatabase.confirm_full_birthdate_invalid_entry = True
            return None

        if BirthDateDatabase.confirm_full_birth_date_input.lower() == "no":
            BirthDateDatabase.confirmed_full_birthdate = False
            return None

        BirthDateDatabase.confirmed_full_birthdate = True


class BirthDateFunctionsControl:
    @staticmethod
    def run():
        """Execute all method's related to birthdate in particular order."""

        BirthDateFunctions.inform_about_birthday()

        while BirthDateDatabase.STARTING_LOOP == True:
            clean()
            BirthDateFunctions.all_loop_values_true()
            BirthDateFunctions.reset_all_birth_operation_variables()
            BirthDateFunctions.add_or_pass_birthdate()

            if (
                not BirthDateDatabase.accepted_to_add_birthdate
                and not BirthDateDatabase.add_or_pass_invalid_entry
            ):
                BirthDateFunctions.warning_diverting_to_main_menu()
                BirthDateFunctions.all_loop_values_false()

            if (
                BirthDateDatabase.add_or_pass_invalid_entry
                and not BirthDateDatabase.accepted_to_add_birthdate
            ):
                BirthDateFunctions.warning_invalid_entry()
                continue

            while BirthDateDatabase.LOOP2 == True:
                BirthDateFunctions.input_birthday()

                if (
                    BirthDateDatabase.input_birth_day_invalid_entry
                    and not BirthDateDatabase.added_birthday
                ):
                    BirthDateFunctions.warning_invalid_entry()
                    continue

                while BirthDateDatabase.LOOP3 == True:
                    BirthDateFunctions.input_birthmonth()

                    if (
                        BirthDateDatabase.input_birth_month_invalid_entry
                        and not BirthDateDatabase.added_birthmonth
                    ):
                        BirthDateFunctions.warning_invalid_entry()
                        continue

                    while BirthDateDatabase.LOOP4 == True:
                        BirthDateFunctions.input_birthyear()

                        if (
                            BirthDateDatabase.input_birth_year_invalid_entry
                            and not BirthDateDatabase.added_birthyear
                        ):
                            BirthDateFunctions.warning_invalid_entry()
                            continue

                        while BirthDateDatabase.ENDING_LOOP == True:
                            BirthDateFunctions.evaluate_full_birthdate()
                            BirthDateFunctions.confirm_birthdate()

                            if (
                                BirthDateDatabase.confirm_full_birthdate_invalid_entry
                                and not BirthDateDatabase.confirmed_full_birthdate
                            ):
                                BirthDateFunctions.warning_invalid_entry()
                                continue

                            if (
                                not BirthDateDatabase.confirmed_full_birthdate
                                and not BirthDateDatabase.confirm_full_birthdate_invalid_entry
                            ):
                                clean()
                                sleep(1)
                                BirthDateFunctions.restart_birthdate_operation()
                                break

                            clean()
                            BirthDateFunctions.warning_birthdate_added_to_account
                            sleep(4)
                            BirthDateFunctions.all_loop_values_false()
