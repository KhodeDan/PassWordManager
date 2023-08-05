

"_____________________ Imports _______________________"


# Import the sleep function from the Built In time module.
from time import sleep 


# Import Os from Python Files.
import os


# Import the sys module , In order to use in the exiting Operation.
import sys


"______________________________________________________"


"__________________ Needed Variables ________________"


version = 'Beta 1.4.9'     # *Semantic Numbering.


# Define a empty dictionary , Which Later Is going to contain Username's , Masterpassword's , Password's.
Users_Info = {
    "Users" : {}
}


# A dictionary of all the avaliable Operation's that can be used in the main menu , All assigned with a number.
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


# Define all the letter's possible to write In a password , Uppercase and Lowercase letter's and number's for further use.
allowed = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ,"0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , ]
UpperCase_Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ,]
LowerCase_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]


# All Case situation's of the word Quit , In order to be used in the quitting situation's
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


"_____________________________ Clearing Function _______________________________"


# Shorted function for os.system('cls')
def clean() -> None:


    os.system('cls')


clean()


"_______________________________________________________________________________"


"______________________________ Loading Look-Function __________________________"


# Define a function called loading_Look , Which Have the order of starting the main loading look at the start of the code.
def loading():
    print("\33[31mLoading Assets....")
    sleep(1)
    clean()
    print("Loading Assets...")
    sleep(1)
    clean()
    print("Loading Assets..")
    sleep(1)
    clean()
    print("Loading Attachments....")
    sleep(1)
    clean()
    print("Loading Attachments...")
    sleep(1)
    clean()
    print("Loading Attachments..")
    sleep(1)
    clean()
    print("Loading Attachments.")
    sleep(1)
    clean()
    print("Loading Done!\33[34m")
    sleep(1)


    clean()


"__________________________________________________________________________"


"_____________________________ Termination (Exiting) Operation __________________________"


# Define a function called termination , Which Have the part of cleaning , Exiting The program In an ordinary way .
def termination():


            clean()


            print("\33[Thanks for Using KhodeDan's Password Manager.")


            sleep(4)


            clean()


            print("\33[1;31;40mQuitting.... \33[0m")


            sleep(3)


            clean()


            sys.exit()   # This syntax used with sys module , Will tell the python interpreter to terminate the project.


"_______________________________ Termination (Exiting) Operation ___________________________"


"_________________________ UserName Checking Function______________________"


# Define a function that will check the Chosen UserName , And see If it meet's the minimum Requirement's.
def isusername(UserName : str):


    UserName_Last_Limit = 13     # Define a variable with the value of 13 , Which Later will be used for the lengh checking of the UserName.
    UserName_First_limit = 3     # Define A variable with the value of 13 , Which Later will be used for the lengh chdcking of the Username.
    UserName_Lengh = len(UserName)   # Check the lengh of the username and store It in a variable.



    if UserName_First_limit > UserName_Lengh :
        return False

    
    
    if UserName_Last_Limit < UserName_Lengh:
        return False
    



    

    if UserName.isdigit():
        return False

    
    for character in UserName:


        if character not in allowed:
            return False
    

    return True




"_________________________ UserName Checking Function______________________"


"_______________________ BirthYear Checking Function _______________________"


# Define a function in order to make sure the user entered birthyear Is correct and logical.  
def isbirthyear(birthyear : int):
    
    # Define a variable with the value of 1923 , Which will act as the lowest birthyear that can be entered.
    Age_First_Limit = 1923
    
    # Define variable with the value of 2022 , Which means the Latest birthyear possible to use this program
    Age_Last_Limit = 2022




    try:
        if birthyear > Age_Last_Limit:
            return False
        

        if birthyear < Age_First_Limit:
            return False
        

        return True
    

    except:
        return False


"_______________________ Birthyear Checking Function ______________________"


"_______________________ BirthMonth Checking Function ______________________"


# Define a function called Is birthmonth in order to make sure a integer has all the needed option's to be counted as a birthmonth.
def isbirthmonth(birthmonth : int):

    try:
    
        birthmonth = birthmonth + 1
        birthmonth_First_Limit = 1
        birthmonth_Last_Limit = 13




        if birthmonth > birthmonth_Last_Limit :
            return False
        
        
        if birthmonth < birthmonth_First_Limit:
            return False


        return True
    
    
    except:
        return False


"_________________________ BirthMonth Checking Function ___________________"


"________________________ BirthDay Checking Function ______________________"


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


"___________________________ Birthday Checking Function __________________________"


"___________________________ MasterPassword Checking Function ___________________"


# define a function called MasterPassword with a string argument in order to make sure a string Has all the option's needed to be counted as a masterPassword.
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

    
"___________________________ MasterPassword Checking Function ___________________"





# Define a function called ispassword , Which will check if the user entry Is a real Password , In this Case , There Isn't much prohibited Case's , Because user may enter different type of Password's (Digit , ETC)
def ispassword(password):
    "------------------ Needed Variables --------------------"
    Password_Firstlimi = 1   # Define a variable with the value of int 1 , Which will act as the limitation for the user entry lengh.
    Password_Lastlimit = 30  # Define a variable with the value of int 50 , Which will act as the limitation for the user entry lengh.
    Password_Lengh = len(password)   # Define a variable which will keep the lengh of the entered password , As value.
    "--------------------------------------------------------"


    if Password_Lengh > Password_Lastlimit:
        return False
    

    if Password_Lengh < Password_Firstlimi:
        return False
    

    return True





"___________________________ MasterPassword Check Function ________________________"


def equality_check(string : str , MasterPassword : str) -> bool:


    if string == MasterPassword:


        return True
    

    return False


"______________________ Value by key __________________"


def get_key_by_value(dictionary : dict , value):
    "Recieve the key of a dictioanry by mentioning It's value"

    
    for key,value in dictionary.items():


        if dictionary[key] == value:


            return key
        

        return None
