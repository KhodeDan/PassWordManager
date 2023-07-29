

"_____________________ Imports _______________________"


# Import the sleep function from the Built In time module.
from time import sleep 


# Import Os from Python Files.
import os


"______________________________________________________"


"__________________ Needed Variables ________________"


version = 'Beta 1.1.0'     # The current version of KhodeDan's Password Manager App. *(Semantic Numbering.)

# Define a empty dictionary , Which Later Is going to contain Username's , Masterpassword's , Password's.
Users_Info = {}


# A dictionary of all the avaliable Operation's that can be used in the main menu , All assigned with a number.
Operations = {1 : "Add_Password" , 2 : "Remove_Password" , 3 : "Change_MasterPassword" , 4 : "Forgot_MasterPassword" , 5 : "Quit"}


# Define all the letter's possible to write In a password , Uppercase and Lowercase letter's and number's for further use.
allowed = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ,"0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , ]
UpperCase_Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ,]
LowerCase_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]


"_____________________________ Clearing Function _______________________________"


# Define a function called clean , Do the Part of cleaning the terminal with Os , In an easier command.
def clean():
    os.system('cls')
clean()


"_______________________________________________________________________________"


"______________________________ Loading Look-Function __________________________"


# Define a function called loading_Look , Which Have the order of starting the main loading look at the start of the code.
def loading():
    print("Loading Assets....")
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
    print("Loading Done!")
    sleep(1)


"__________________________________________________________________________"


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


