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
                    Users_Info["Users"][Inputted_Username]["PassWords"] = {}
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


                                            Birth_Date = F"{Birth_Day}/{Birth_Month}/{Birth_Year}"

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
    Users_Info = {"Users" : {


        "KhodeDan" : {



            "MasterPassword" : "RedWolf1388",



            "PassWords" : {}, 



            "Birth_Date" : "1/1/1980" ,



            },


            "Eminem" : {
                

                "MasterPassword" : "Hello-World"
            },


        }, 


    }


    Inputted_Username = "KhodeDan"
    "-------------------------- Needed Variables ------------------------"
    LOOP1 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP2 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP3 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP4 = True     # Define A bool (True) Variable In order to ube used as FLAG variable in the looping operation.
    LOOP5 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP6 = True     # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP7 = True     # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP8 = True     # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP9 = True     # Define A bool (True) Variable In order to be used as FLAG varibale in the forgot Password Operation Looping.
    LOOP10 = True    # Define A bool (True) Variable In order to use in the Change User Operation.
    LOOP11 = True    # Define A bool (True) Variable In order to use in the Change User Operation.
    users_count = len(Users_Info["Users"])   # Define a variable Which keeps the lenght of the Users count as variable.
    changeuser_MasterPassword_Inbox = ""     # Define a variable with the value of str ("") In order to be used as MasterPassword Input in change user Operation.
    changeuser_username_Inbox = ""   # Define A variable with the value of str ("") In order to be used as UserName input in the change user operation.
    ForgotOperation_NewMasterPassword_inbox = ""     # Define A variable with the value of str ("") In order to be used as the NewMasterPassword Input in the forgot Password Operation
    ForgotOperation_BirthDate = ""   # Define A variable with the value of str ("") In order to be used in creating the new BirthDate in the forgot MasterPassword Operation.
    BirthDate_Check = ""  # Define A variable with the value of str ("") In order to be used to check If the user have a existing Birth_Date in their Info or not To be used in the forgot MasterPassword Operation
    Birth_Day_Inbox = ""     # Define A str ("") Variable In order to be used as BirthDay Input identifier In the forgot MasterPassword Operation.
    Birth_Month_Inbox = ""   # Define A str ("") Variable In order to be used as BirthMonth Input Identifier In the forgot MasterPassword Operation.
    Birth_Year_Inbox = ""    # Define A str("") Variable in order to be used as BirthYear Input Identifier In the forgot MasterPassword Operation.
    Current_MasterPassword = Users_Info["Users"][Inputted_Username]["MasterPassword"]    # Define a variable with the value of The user Current MasterPassword (Titled) , In order to be used in the MasterPassword Concerned Operation's.
    User_Desired_Operation = ""    # Define A str ("") Value Variable in Order to be used as the User Input storing Variable , In order to understand what operation they want to use.\
    MasterPassword_Inbox = ""    # Define A str ("") Value variable In order to use as an input , In the changing MasterPassword Operation.
    New_MasterPassword_Inbox = ""    # Define A str ("") Value Variable In order to use as an input , In the changing MasterPassword Operation.
    PassWord_Title = ""  # Define A str ("") Value variable , In order to keep the name of the password.
    Desired_PassWord = ""    # Define A str ("") Value variable in Order to store the password that the user want's to add in the Add_Password.\
    Want_To_Remove = ""     # Define A str("") Value Variable in Order to store the password that Is going to be deleted.
    PassWords = "PassWords"  # Define A str ("PassWords") Value variable in Order to use in A F string print (In order to avoid quotation mark.)
    Number = 1   # Define A int (1) Value variable In order to use as numbering in the loop.
    "--------------------------------------------------------------------"


    # Start a while Loop With the condition Of the first FLAG variable to be True , In order to LOOP through the menu and It's option's.
    while LOOP1 == True:
        

        clean()


        # Define an If statement , If the First Flag Variable
        if LOOP1 == False:
            break

        
        print("\33[34m\33[40m Here Are all the operation's You can use (Insert the Number of Operation In order to use): ")
        

        # Start a for loop that iterate Over all Operation's In the operation Dictionary and they're key Number , In order to print them one by one.
        for Operation_Number , Operation in Operations.items():


            print(F"{Operation_Number} . {Operation} ")
        


        print("")


        print("\33[31m---------------------- User Management -----------------------------")


        print("")


        for user_operation_number , user_management_operation in user_management_operations.items():


            print(F"\33[34m{user_operation_number} . {user_management_operation}")
        

        print("")


        User_Desired_Operation = input("What Operation Would you like to choose?(Operation Number) : ")


        if User_Desired_Operation.isdigit():


            User_Desired_Operation = int(User_Desired_Operation)
            

        else:


            clean()


            print("That Is not a known Operation Code name.")
            print("Please try again.")


            sleep(3)
        

        # VIEW PASSWORD.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 1]:
    
    
            if len(Users_Info["Users"][Inputted_Username]["PassWords"]) == 0:
    
    
                clean()
    
    
                print(F"You currently Have no Password's stored . You can store password's in the password adding menu.")
                print("Returning to the main menu")
    
    
                sleep(5)
    
    
                continue
    
    
            else:
    
    
                clean()
                    
    
                print("Here Are all the Password's You've stored : ")
                print("")


                Number = 1


                for PassWord,Title in Users_Info["Users"][Inputted_Username]["PassWords"].items():
                            
                        
                    print(F"{Number} . {PassWord} : {Title}")
                    print('')


                    Number = Number + 1


                print("")
                input("Press any key to return to the main menu.")
    
    
        # ADD PASSWORD.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 2]:
    
    
            LOOP2 = True
    
    
            while LOOP2 == True:
                        
    
                clean()
    
    
                if LOOP2 == False:
                    break
    
    
                Desired_PassWord = str(input("Please enter the Password you would like to add : "))

                clean()


                PassWord_Title = str(input("Now Please enter the title you want to specify the password : "))


                clean()


                # This If statement will check ( If the Entered password Is not an empty string and if the entered Password Allready Don't exist in the User passwords )
                if ispassword(Desired_PassWord) and Desired_PassWord not in Users_Info["Users"][Inputted_Username][PassWords]:
    
    
                    Users_Info["Users"][Inputted_Username]["PassWords"][Desired_PassWord] = PassWord_Title
    
    
                    print(F" {Desired_PassWord} Has been added to your password's list as {PassWord_Title}")
                    print("Diverting to the main menu.")
    
    
                    sleep(5)


                    LOOP2 = False

        
                # And if the password Allready exist In the password's dictionary , The User will be notified.
                else:
    
    
                    clean()
    
    
                    print("That Password Allready exist's in Your password's list.")
                    print("Please try again.")
    
    
                    sleep(3)
    
    
                    continue  
        

        # REMOVE-DELETE PASSWORD.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 3]:


            LOOP3 = True


            while LOOP3:


                if LOOP3 == False:
                    break


                clean()


                if len(Users_Info["Users"][Inputted_Username][PassWords]) == 0:


                    print("You currently Have no Password Stored , You can add password's using the Add Password Option In the menu.")
                    print("Diverting Back to the menu...")


                    sleep(4)


                    clean()


                    LOOP3 = False

                
                else:


                    Number = 1


                    for PassWord,PassWord_Title in Users_Info["Users"][Inputted_Username][PassWords].items():


                        print(F"{Number} . {PassWord} : {PassWord_Title}")
                        print("")


                        Number = Number + 1

                    print("Write the PassWord name only.")
                    Want_To_Remove = input("Which One of theese Password's Would you like to delete? : ")


                    if Want_To_Remove == PassWord in Users_Info["Users"][Inputted_Username][PassWords].keys():


                        deleted_PassWord = Users_Info["Users"][Inputted_Username][PassWords].pop(Want_To_Remove)


                        clean()


                        try:


                            print(F"{deleted_PassWord} has been deleted.")


                            del deleted_PassWord


                        except:


                            clean()
                            

                            print("The Inserted Password does not exist , Please try again.")


                            continue


                        sleep(3)


                        LOOP3 = False ; break
                    

        # CHANGE MASTERPASSWORD
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 4]:


            while LOOP4 == True:


                if LOOP4 == False:
                    break


                clean()


                print("Change MasterPassWord Menu :")
                print("")
                print("1. Remember You can Insert quit For returning to the main menu If you changed your mind.")


                MasterPassword_Inbox = input("Please enter your Current MasterPassword to Resume : ")
                MasterPassword_Inbox = MasterPassword_Inbox.strip()


                if MasterPassword_Inbox == Current_MasterPassword:


                    clean()

                    
                    print("Access granted.")

                    
                    sleep(3)

                    
                    LOOP4 = False


                    LOOP5 = True


                    while LOOP5 == True:


                        clean()

                        print("Remember that If you changed your mind , You can type in quit for returning to the main menu")
                        print("The Inserted MasterPassword Must Contain At least 1 UpperCase , LowerCase Letter , And A Number.")
                        print("")
                        New_MasterPassword_Inbox = input("Please type In your new MasterPassword : ")
                        New_MasterPassword_Inbox.strip()


                        if ismasterpassword(New_MasterPassword_Inbox):


                            try:

                                Users_Info["Users"][Inputted_Username]["MasterPassword"] = New_MasterPassword_Inbox


                                # Change the current password variable In order to avoid Upcoming Error's everytime the operation Rerun's.
                                Current_MasterPassword = Users_Info["Users"][Inputted_Username]["MasterPassword"]


                                clean()


                                print(F"{New_MasterPassword_Inbox} Has been set as your MasterPassword.")


                                sleep(2)


                                print("Diverting to the main menu...")


                                sleep(3)


                                LOOP5 = False


                            except:


                                print("The Operation was unsuccesfull , Please try again Later.")


                                LOOP5 = False
                        

                        # Checks if the user Typed in any form of the word "QUIT"
                        elif New_MasterPassword_Inbox in QUIT_LETTERCASE:


                            clean()


                            sleep(1)


                            print("Returning to the main menu...")


                            sleep(3)


                            LOOP5 = False

                        

                        else:


                            clean()


                            print("The entry Cannot be accepted as A MasterPassword , Please try again.")


                            sleep(3)


                            continue



                elif MasterPassword_Inbox in QUIT_LETTERCASE:


                    clean()


                    print("The Operation Has been Cancelled.")


                    sleep(2)


                    print("Diverting to the main menu...")


                    sleep(3)


                    break


                else:


                    clean()
                    sleep(2)


                    print("Access Denied.")


                    sleep(2)


                    continue

        
        # FORGOT MasterPassword.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 5]:


            BirthDate_Check = Users_Info["Users"][Inputted_Username].get("Birth_Date" , False)


            if BirthDate_Check == "Birth_Date":


                LOOP6 = True
            

            else:


                clean()

                
                sleep(1)


                print("")


                print("You Have not added Your birthday to your account , You can't recover your MasterPassword .")


                sleep(5)


                LOOP6 = False


                continue

            
            while LOOP6 == True:


                clean()

                
                print("Remember You can type in QUIT Anytime you have changed your mind.")


                print("Right Now , There Is only one solution for the Password Recovery Operation.")


                sleep(2)


                print("")





                Birth_Day_Inbox = input("Please Type In your Birth Day (1 TO 31) : ")


                if Birth_Day_Inbox in QUIT_LETTERCASE:


                    break


                if Birth_Day_Inbox.isdigit():


                    Birth_Day_Inbox = int(Birth_Day_Inbox)

                

                else:


                    clean()


                    print("The entry Is not a number , Please try again.")


                    sleep(2)


                    continue


                if isbirthday(Birth_Day_Inbox):


                    LOOP7 = True


                    while LOOP7 == True:


                        clean()


                        


                        print("Remember You can type in QUIT , for returning to the main menu.")


                        Birth_Month_Inbox = input("Now Please Type in the month you were born (1 to 12) :  ")


                        if Birth_Month_Inbox in QUIT_LETTERCASE:


                            LOOP7 = False
                            LOOP6 = False
                            

                        elif Birth_Month_Inbox.isdigit():


                            Birth_Month_Inbox = int(Birth_Month_Inbox)


                            if isbirthmonth(Birth_Month_Inbox):


                                LOOP8 = True


                                while LOOP8 == True:


                                    clean()

                                        
                                    Birth_Year_Inbox = input("At Last , Please type in the year you were born (1923 , 2022) : ")


                                    if Birth_Year_Inbox in QUIT_LETTERCASE:


                                        LOOP6 = False
                                        LOOP7 = False
                                        LOOP8 = False


                                        break


                                    if Birth_Year_Inbox.isdigit():


                                        Birth_Year_Inbox = int(Birth_Year_Inbox)

                                            
                                        if isbirthyear(Birth_Year_Inbox):


                                            ForgotOperation_BirthDate = F"{Birth_Day_Inbox}/{Birth_Month_Inbox}/{Birth_Year_Inbox}"


                                            if ForgotOperation_BirthDate == Users_Info["Users"][Inputted_Username]["Birth_Date"]:


                                                LOOP9 = True


                                                while LOOP9 == True:


                                                    clean()


                                                    print("Now , You should enter the new MasterPassword you would like.")
                                                    print("")
                                                    print("MasterPassword Must have at least 1 Upper case and lowerCase letter , 1 Number , Shouldn't be less than 5 characters.")


                                                    ForgotOperation_NewMasterPassword_inbox = input("Please enter the new MasterPassword : ")
                                                    ForgotOperation_NewMasterPassword_inbox = ForgotOperation_NewMasterPassword_inbox.strip()


                                                    if ismasterpassword(ForgotOperation_NewMasterPassword_inbox):


                                                        ForgotOperation_NewMasterPassword_inbox = Users_Info["Users"][Inputted_Username]["MasterPassword"] 


                                                        print(F"{ForgotOperation_NewMasterPassword_inbox} Has been chosen as your new MasterPassword.")


                                                        sleep(4)


                                                        LOOP9 = False
                                                        LOOP8 = False
                                                        LOOP7 = False
                                                        LOOP6 = False
                                                    

                                                    else:


                                                        clean()


                                                        print("Remember that the MasterPassword should have at least 1 uppercae letter , 1 LowerCase letter , And 1 number.")


                                                        print("That Is not a MasterPassword , Please try again.")


                                                        sleep(4)


                                            else:


                                                clean()


                                                print("Access denied , Returning to the menu.")


                                                LOOP6 = False
                                                LOOP7 = False
                                                LOOP8 = False


                                        else:


                                            clean()


                                            print("The Inserted Content is not a BirthYear , Please try again.")


                                            sleep(4)

                                    
                                    else:

                                        clean()


                                        print("The inserted content Is not a Number , Please try again.")


                                        sleep(4)
                                        
                                
                            else:


                                clean()


                                print("The entry Is not a birthmonth , Please try again.")


                                sleep(4)


                        else:


                            clean()


                            print("The entry Is not a Number , Please try again.")


                            sleep(4)
                        

                else:


                    clean()


                    print(" The Inserted Number Is not a BirthDay , Please try again.")


                    sleep(4)
        

        # CHANGE USER.
        if User_Desired_Operation in [Number for Number in user_management_operations.keys() if Number == 7]:


            if users_count == 1:


                clean()

                
                print("You Have no other account's , You can add Other Account's using add user button in the menu.")

                
                clean()


                continue


            else:


                LOOP10 = True


                while LOOP10 == True:


                    clean()


                    print("\33[31mHere are all the avaliable accounts : \33[34m")


                    print("")


                    for user in Users_Info["Users"]:


                        print(F"⁛  {user} ⁛")
                        

                        print("")

                    
                    sleep(1)


                    print("Remember you can type in \33[31mquit\33[34m for returning to the main menu , Anytime you desire.")


                    changeuser_username_Inbox = input("Which one of the \33[31maccount's\33[34m would you like to Login ? (\33[31mAccount Name\33[34m): \33[0m")
                    changeuser_username_Inbox = changeuser_username_Inbox.strip()


                    if changeuser_username_Inbox in [user for user in Users_Info["Users"] if changeuser_username_Inbox == user] and changeuser_username_Inbox != Inputted_Username:


                        clean()


                        LOOP11 = True


                        while LOOP11 == True:


                            clean()


                            changeuser_MasterPassword_Inbox = input(F"\33[34mPlease enter the \33[31m MasterPassword\33[34m For the account \33[31m{changeuser_username_Inbox}\33[0m : ")
                            changeuser_MasterPassword_Inbox = changeuser_MasterPassword_Inbox.strip()


                            if changeuser_MasterPassword_Inbox == Users_Info["Users"][changeuser_username_Inbox]["MasterPassword"]:


                                clean()


                                print(F"\33[34m Successfully Logged Into account \33[31m{changeuser_username_Inbox}\33[34m")


                                Inputted_Username == changeuser_username_Inbox


                                sleep(5)


                                LOOP10 = False
                                LOOP11 = False
                            

                            elif changeuser_MasterPassword_Inbox in [quit_type for quit_type in QUIT_LETTERCASE if changeuser_MasterPassword_Inbox == quit_type]:


                                clean()


                                print("Quitting to the main menu.")


                                LOOP10 = False
                                LOOP11 = False
                            

                            else:


                                clean()


                                print("\33[31mAccess denied.\33[34m")


                                sleep(3)


                                LOOP11 = False


                    elif changeuser_username_Inbox in [quit_type for quit_type in QUIT_LETTERCASE if changeuser_username_Inbox == quit_type]:


                        clean()


                        print("Quiting to the main menu.")


                        sleep(2)


                        LOOP10 = False
                    

                    elif changeuser_username_Inbox == Inputted_Username:


                        clean()


                        print(F"\33[31mYou are allready Logged Into account \33[31m{changeuser_username_Inbox} \33[34m")

                        
                        sleep(4)


                        clean()
                    

                    else:


                        clean()


                        print("\33[31mThat Account UserName does not exist , try again.\33[34m")


                        print("")


                        print("Please note that All account usernames are \33[31m cAsE sEnSiTiVe\33[34m")


                        sleep(5)


        # Quitting Operation.
        elif User_Desired_Operation in [Number for Number in Operations.keys() if Number == 6]:


            # One of the database Defined Function's , Which will terminate the program In a ordinary way , With a comfy GoodBye Message!
            termination()


"--------------------------- Main Menu Function (End) -------------------"


Main_Menu()