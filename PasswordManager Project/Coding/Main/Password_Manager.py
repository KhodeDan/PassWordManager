"___________________________ Importing ___________________________________"


# Import All neded variable's and exponent's from The Database.
from Database.Data import *


"__________________________________________________________________________"


# Define a function That will make the starting Operation Of the app.
def starting():


    "---------------------------- Loading Look --------------------------------"


    # Call the function Loading Look , One of the Database Made function's that will make The Code Look like a loading screen
    loading()


    "--------------------------------------------------------------------------"


    "---------------------------- welcoming -----------------------------------"


    print(F"Welcome to KhodeDan Password Manager version : {version}")
    sleep(4)


    "--------------------------- welcoming ------------------------------------"






"------------------------- UserName collecting Function(Start) ----------------------------"


# Define a function Called Welcoming , Which Have the Order Of initializing the start of the code.
def Collect_UserName():


    clean()


    "--------------- Loop Variables ----------------"
    LOOP1 = True     # Define a variable with the value of True , Which Later act's as a flag variable.
    LOOP2 = True     # Define a variable with the value of True , Which Later act's as a flag variable.
 
    UserName_Yes_No = None   # Define a variable Called UserName_Yes_no with NoneType value , Which later act's as a variable for asking the user If theirre sure about their entry. 
    "-----------------------------------------------"


    clean()  # Clean Is a replacement function for os.system('cls')


    sleep(4)


    # Start a while loop that will be repeted to CONFIRM or DECLINE the user entry.
    while LOOP1:
        clean()


        # Make an If statement In order to break the loop and finish the program If needed.
        if LOOP1 == False:
            break

        
        print('')
        print("Note That Username's can only contain Uppercase , LowerCase Letters , Number's")
        global Inputted_Username
        Inputted_Username = input("Please Chose a userName For Your account : ")


        
        if isusername(Inputted_Username):

            sleep(1)
            clean()


            # Start A while loop In order to repeat the Asking operation.
            while LOOP2:
                clean()


                # Define and if statement to make sure the loop will break Once the Flag variable Is set to False.
                if LOOP2 == False:
                    break


                UserName_Yes_No = input(F"Are You sure you want {Inputted_Username} As your account userName? (Answer With yes or no only)  : ")
                UserName_Yes_No = UserName_Yes_No.lower() ; UserName_Yes_No = UserName_Yes_No.strip()
                # Turn all the letter's in The user entry to lowerCase and delete all spaces , In order to make the recognizing Easier.


                if UserName_Yes_No == "yes":
                    clean()


                    Users_Info["Users"] = {Inputted_Username : {}}


                    print(F"{Inputted_Username} Has been chosen as your username.")
                    sleep(3)
 


                    # Set All loop variables to false , In order to finish the welcoming Program.
                    LOOP1 = False
                    LOOP2 = False
                    break


                elif UserName_Yes_No == "no":
                    clean()


                    print("Returning to the login Panel")
                    sleep(3)
                    break


                else:
                    clean()
                    print("That Is not a yes or no , Please try again.")
                    sleep(3)


        else:
            clean()
            print("This username does not meet the requirement's to be used. \n\
                  Please note that usernames : \n \
                  1. Should Not be less than 3 characters .\n \
                  2. Should Not be more than 13 characters.\n \
                  3. Should Not be number's only.\n \
                  4. Usernames can only contain Uppercase And Lowercase letters , Numbers.  ")         
            input("Press any key to try again")


"------------------------------ UserName Taking Function(END) -------------------------------"


"-----------------------------  MasterPassword Taking function(Start) ---------------------------"


# Define a function called collect_user_info , Which will collect the BirthTime of the user for the recovery operation and will collect a MasterPassword.
def collect_MasterPassword():
    "--------------------- Needed variables -------------------"
    global Inputted_MasterPassword   # Turn the Inputted_MasterPassword Variable to a global variable.
    Inputted_MasterPassword = None   # define a variable with the value of None which later will be user for collecting the user MasterPassword Entry.
    MasterPassword_Add_Retry = ""  # Define a variable with the value of "" string which Later will be user for asking the user wether they are sure abou their masterpassword entry ot not.
    LOOP1 = True     # Define a variable with the bool (True) Value In order to use as a FLAG variable in the looping Operation.
    LOOP2 = True    # Define a variable with the bool (True) Value In order to use as a flag variable for the loop operation.
    LOOP3 = True     # Define a variable with the bool (True) Value In order to use as a flag variable for the loop operation .
    "--------------------- Needed variables -------------------"
    clean()


    # This Part of the code have been initialized In a while loop In order to avoid Upcoming Errors , DO NOT REMOVE THE WHILE LOOP.
    while LOOP1 == True:


        if LOOP1 == False:
            break


        print("This Is the part where you should chose a MasterPassword.")
        print("This MasterPassword will be used for accessing your account.")
        print("Do not share It with anyone.")
        input("Press any key to contoniue.")


        LOOP1 = False
        break


    # Define a while loop in Order to loop through the password Choosing Operation.
    while LOOP2 == True:


        clean()  


        # Define the loop breaker if statement of the operation. (Flag Variable)
        if LOOP2 == False:
            break


        print("The MasterPassword at least Must have 1 Upper Case letter , 1 LowerCase Lettter , And at least A number.")
        Inputted_MasterPassword = input(F"Please Chose a MasterPassword for the account {Inputted_Username} : ")
        Inputted_MasterPassword.strip()  # Delete all spaces from the user inputted masterpassword.


        if ismasterpassword(Inputted_MasterPassword):


            # Start a while loop In order to ask the user if their sure about their Inputted MasterPassword.
            while LOOP3:


                clean()
                

                # Define the loop breaker If statement. (Flag variable)
                if LOOP3 == False:
                    break

                
                print("Answer with yes or no only.")
                MasterPassword_Add_Retry = input(F"Are You sure you want {Inputted_MasterPassword} As Your MasterPassword ? : ")
                MasterPassword_Add_Retry = MasterPassword_Add_Retry.lower() ; MasterPassword_Add_Retry = MasterPassword_Add_Retry.strip()
                # Turn the first lettter of the entry to uppercase , And delete all spaces from the left and right side.


                # Define an if statement , If the User Is sure about their decision , The MasterPassword Will be On their Username.
                if MasterPassword_Add_Retry == "yes".lower():

                    Users_Info["Users"][Inputted_Username] = {}
                    Users_Info["Users"][Inputted_Username]["MasterPassword"] = Inputted_MasterPassword
                    print(F"{Inputted_MasterPassword} Has Been chosen as your MasterPassword")
                    sleep(3)
                    clean()
                    LOOP1 = False ; LOOP2 = False ; LOOP3 = False 
                    break


                # Define an if statement , If the user Change their mind about the Passsword , They will be returned to the password Choosing menu.
                elif MasterPassword_Add_Retry == "no".lower():
                    clean()
                    print("Returning to the PassWord Choosing Menu...")
                    sleep(3)
                    break
                


            



"---------------------------- MasterPassword Taking Function(End) -----------------------"


"---------------------------- BirthDate taking Function(Start) --------------------------"


# Define a Function that will ask the user if they want to add their birthday or not , And Will append the birthdate to the account Information If added.
def Collect_BirthDate():
    "----------------------- Needed Variables -----------------------"
    BirthDate_Add_Pass = None    # Define a variable with the NoneType value Which will be used to ask the user if they want to add their birthdate or not.
    Birth_Day = None     # Define a variable with the the NoneType value which will be used As the day of the user birth.
    Birth_Month = None   # Define a variable with the NoneType value which will be used as the month of the user birth.
    Birth_Year = None    # Define a variable with the NoneType value which will be used as the year of the user birth
    Birth_Date = None    # Define a variable with the NoneType value which will be used as the full birthdate (YY/MMM/DD)
    Date_Yes_No = None   # Define variable with the NoneType value which will be used as the input variable to make sure if the user accept the date as their birthdate.
    LOOP1 = True     # Define a variable with the  bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP2 = True     # Define a variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP3 = True     # Define a variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP4 = True     # Define a variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP5 = True     # Define a variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    "----------------------- Needed Variables -----------------------"


    clean()

    
    print("Now that you have a MasterPassword , You need a way for recovering It If needed.")
    print("In this case , You can add your BirthDate for the recovery Operation.")
    input("Press any key to continue.")


    # Start A While loop In order to ask the user If they want to add their birthdate or not.
    while LOOP1 == True:

    
        clean()

        
        # Define the If statement of the brekaing operation with A Flag Variable.
        if LOOP1 == False:
            break

        print("Answer with Yes or no only.")
        BirthDate_Add_Pass = input("Would You like to Add your birthdate for the recovery Operation? : ")
        BirthDate_Add_Pass = BirthDate_Add_Pass.lower() ; BirthDate_Add_Pass.strip()
        # Turn all the letter's in the User entry to LowerCase , Delete All spaces at the left and right side.


        if BirthDate_Add_Pass == "yes":


            while LOOP2 == True:


                clean()


                if LOOP2 == False:
                    break


                try:
                    Birth_Day = int(input("Please enter the day you were born (1 To 31) : "))
                

                except:


                    clean()
                    continue
                


                if isbirthday(Birth_Day):


                    while LOOP3 == True:


                        clean()


                        if LOOP3 == False:
                            break


                        try:


                            Birth_Month = int(input("Please enter your BirthMonth(1 To 12) : "))



                                

                        except:
                                    

                            clean()
                            continue


                        if isbirthmonth(Birth_Month):


                            while LOOP4 == True:


                                clean()


                                if LOOP4 == False:
                                    break


                                try:


                                    Birth_Year = int(input("Please enter the year you've been born (1923 TO 2022) : "))


                                    if isbirthyear(Birth_Year):
                                        clean()

                                        while LOOP5 == True:


                                            clean()


                                            if LOOP5 == False:
                                                break


                                            Birth_Date = F"{Birth_Day} / {Birth_Month} / {Birth_Year}"

                                            print("Answer with yes or no only.")
                                            Date_Yes_No = input(F"Are You sure You accept This date as birthdate : {Birth_Date} : ")
                                            Date_Yes_No = Date_Yes_No.lower() ; Date_Yes_No = Date_Yes_No.strip()


                                            if Date_Yes_No == "yes":


                                                Users_Info["Users"][Inputted_Username]["Birth_Date"] = Birth_Date
                                                

                                                print(F"{Birth_Date} Has Been Chosen as your account Birthday.")
                                                print("Diverting to the main menu.")
                                                sleep(3)


                                                LOOP1 = False
                                                LOOP2 = False
                                                LOOP3 = False
                                                LOOP4 = False
                                                LOOP5 = False





                                        

                                        else:
                                            clean()
                                            continue

                                
                                except:


                                    clean()
                                    continue






                        

                
                else:
                    print("That Is not a a birthday. Please try again.")
                    input("Press any key to retry.")



            



        elif BirthDate_Add_Pass == "no":
            

            clean()
            

            print("Diverting to the menu...")
            

            sleep(3)


            LOOP1 = False


"---------------------------- BirthDate Taking function (End)--------------------"


"------------------------------ Main Menu function (Start) ----------------------"


# Define a function Named Main Menu , Which Act's as the main menu of the password manager , Containing All the operation's the user can use.
def Main_Menu():
    "-------------------------- Needed Variables ------------------------"
    LOOP1 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP2 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    Desire = None    # Define a NoneType Value Variable in Order to be used as the User Input storing Variable , In order to understand what operation they want to use.
    "--------------------------------------------------------------------"


    # Start a while Loop With the condition Of the first FLAG variable to be True , In order to LOOP through the menu and It's option's.
    while LOOP1 == True:
        

        clean()


        # Define an If statement , If the First Flag Variable
        if LOOP1 == False:
            break

        
        print("Here Are all the operation's You can use (Insert the Number of Operation In order to use): ")

        # Start a for loop that iterate Over all Operation's In the operation Dictionary and they're key Number , In order to print them one by one.
        for Operation_Number , Operation in Operations.items():


            print(F"{Operation_Number} . {Operation} ")

        try:
            Desire = int(input("What Operation Would you like to choose?(Operation Number) : "))
        

        except:

            continue


Main_Menu()


        






