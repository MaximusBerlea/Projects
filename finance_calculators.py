import math
def main(): #defining the program allows me to easily restart while loop
    # Menu shows all the interactions that the user can have with the program
    print("----MENU---- ")
    print("\n*Investment* - To calculate the amount of interest you will earn on your investment")
    print("*Bond* - To calculate the amount you will have to pay on a home loan")
    print("*Exit* - Terminate the program.")

    # .lower() makes sure that the user input is always standardised in lowercase allowing for easier manipulation
    user_option = input("\nEnter either 'Investment' or 'Bond' or 'Exit' to proceed: ").lower()

    # Storing multiple styles of the same word as a contingency agaist user error
    invest = ['investment','invest']
    bond = ['bond']
    leave = ['exit','leave','quit']

    x=False 
    while True:
        
        if user_option in invest:
            print("Would you like to calculate simple or compound interest?")
            investment_option = input("Enter simple or compound here: ").lower()
           
            simple = ['simple']
            compound = ['compound']
           
            principle = 0
            rate = 0
            time = 0 
            #This is the simple interest loop
            if investment_option in simple:
                while True:
                    principle = float(input("\nEnter the principle amount here: "))
                    if principle <= 0:
                        print("Principle amount cannot be less than or equal to zero")
                    else:
                        break

                while True:
                    rate = float(input("Enter the interest rate here: "))
                    rate = rate / 100
                    if rate <= 0:
                        print("Interest rate cannot be less than or equal to zero")  
                    else:
                        break      

                while True:
                    time = float(input("Enter the time in years here: "))
                    if time <= 0:
                            print("Time cannot be less than or equal to zero")  
                    else:
                        break
                            
                total = principle * (1 + rate * time)
                print(f"\nBalance after {time} year/s: £{total:.2f}")
                print("\nThanks for using the simple interest calculator, Returning to menu.")
                main()
                break
            #This is the compound interest loop      
            if investment_option in compound: 
                while True:
                    principle = float(input("\nEnter the principle amount here: "))
                    if principle <= 0:
                        print("Principle amount cannot be less than or equal to zero")
                    else:
                        break

                while True:
                    rate = float(input("Enter the interest rate here: "))
                    rate = rate / 100
                    if rate <= 0:
                        print("Interest rate cannot be less than or equal to zero")  
                    else:
                        break      

                while True:
                    time = float(input("Enter the time in years here: "))
                    if time <= 0:
                            print("Time cannot be less than or equal to zero")  
                    else:
                        break
                    
                
                total = principle * math.pow((1 + rate), time)
                 
                print(f"\nBalance after {time} year/s: £{total:.2f}")
                print("\nThanks for using the compound interest calculator, Returning to menu.")
                main()
                break
        #This is the bond repayment loop
        if user_option in bond: 
            house_value = 0
            bond_rate = 0
            bond_time = 0 

            while True:
                house_value = float(input("\nEnter the present value of the house here: "))
                if house_value <=0:
                    print("House value amount cannot be less than or equal to zero")
                else:
                    break

            while True:
                    bond_rate = float(input("Enter the interest rate here: "))
                    if bond_rate <= 0:
                        print("interest rate cannot be less than or equal to zero") 
                    else:
                        break       

            while True:
                    bond_time = float(input("Enter the number of months here: "))
                    if bond_time <= 0:
                        print("Time cannot be less than or equal to zero")  
                    else:
                        break
          
            br = (bond_rate / 100) / 12
            bond_payment = (br *house_value) / (1 - (1 + br)**(-bond_time))
            
        
            print(f"\nAmount to be paid each month: £{bond_payment:.2f}")
            print("\nThanks for using this bond calculator, Returning to menu.")
            main()
            break
        #Terminates program through x=False
        if user_option in leave:
                print("Thank you for using this program. Have a good day!")
                x
                break
        else:# Else statement provides an error message when user provides incorrect inputs 
         print("Invalid input, Please try again")
         main()
         break
main()

    

          
      
        
        



    

