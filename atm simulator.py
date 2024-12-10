import time
print("Welcome to the ATM!\n")
#Display a prompt to insert the card
print("please insert your card...:")

#Simulate a delay to mimic real ATM behavior
time.sleep(4)

#starting balance and pin
password=1234 #default pinand balance
balance=5000

#simple string to store transcaction
transaction_history=""

#ask for the pin
pin=int(input("Enter your pin:"))

#check if the pin is correct
if pin == password:
    while True:
      #("Display the menu of the options")
        print("\n1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit\n")
        try: #ask the user to select an option    
            option = int(input("Please select an option:\n "))
        except:
            print("please enter valid option")
            continue

        #option 1:check balance
        if option == 1:
            print(f"your current balance is {balance}")
            print("************\n")

            transaction_history += f"Checked balance:{balance}\n"

        # Option 2: Withdraw Cash
        if option==2:
            withdraw_amount=int(input("Enter the amount to withdraw:"))
            print("************\n")

            if withdraw_amount<=balance:
                balance=balance-withdraw_amount

                print(f"{withdraw_amount} is debited from your account")
                print("************")

                print(f"your current balance is: {balance}")
                print("************")

                transaction_history+=f"withdrew: {withdraw_amount}\n"
            else:
                print("insufficient balance")

        # Option 4: Change PIN

        if option==3:
            deposit_amount=int(input("please Enter deposit amount:"))
            print("************")
            #add the amount to the balance
            balance=balance+deposit_amount

            print(f"{deposit_amount} is credited to your account")
            print("************")

            print(f"\nYour new balance is: {balance}")
            print("************")

            transaction_history+=f"Deposited: {deposit_amount}\n"

        #Option 4:Change the account pin
        if option==4:
            new_pin=input("Enter your new pin\n:")
 
            password=new_pin
            #Update the pin
            print("Your PIN has been changed successfully.")
            print("************")

            transaction_history+="changed pin\n"
        #option 5:Display the tranaction history
        if option==5:
            if transaction_history == "":
                print("No transactions yet.")
            else:
                print("\nTransaction History:")
            
        #option 6:Exit the program
        if option==6:
            print("thank you for using the ATM")
            print("************=")

        break
#handle invalid pin 
else:
    print("wrong PIN. please try again.")

