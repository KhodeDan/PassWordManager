# language: en


Feature: Signing panel
 
 A program with only a sign-up feature would not be able
 to provide multifarious interaction with its users
 in a expected exceptional manner. 
 Although, the idea of having a signing panel
 would not only indiciate this problem, but
 also provide a great methodology for implementing
 the sign-in feature.

 
 Scenario: The app is launched
  Given The user launches the app
    And The loading operation has succeeded
    And the user is greeted by the app

   Then Show the signing panel

  But if by any mean, the application have been interrupted
   Then safely close the app interface and clean the terminal


 Scenario: the sign-in option is decided
  Given the login panel is shown
   When the user choose the sign-in option
    Then take the user app username

   When the username is validation checked
    And the username is found valid
    And the username exists in the database
     Then take the users masterpassword
    
    But if by any mean, the username was not found valid
     Then inform the user
     And return to the base signing panel

   Given the masterpassword is validation checked
    And the masterpassword is found valid
    And the inserted masterpassword is the one that is alligned to the username
     Then log in
     And take the user to the main menu
   
    But if by any mean, the masterpassword was not found valid
     Then Inform the user
     And return to the base signing panel


 Scenario: The sign-up option is decided
  Given the login panel is shown
   When the user choose the sign-up option
   Then guide the user through the account
    creating operation.

 # This scenario is allready implemented
 # to the codebase, due to changes 
 # applied to the project management
 # principles, this scenario and all
 # the code components before the shift
 # are left unsupported in the new
 # BDD principle.