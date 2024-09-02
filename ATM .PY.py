import time

password = 1234
balance = 10000

print("Please insert your CARD")
time.sleep(1)

# Request the user to enter their PIN
pin = int(input("Enter your ATM PIN: "))

if pin == password:
    while True:
        print("""
        1 - Check balance
        2 - Withdraw balance
        3 - Deposit balance
        4 - Balance transfers
        5 - Exit
        """)
        try:
            option = int(input("Please enter a valid option: "))

            if option == 1:
                print(f"Your current balance is {balance}")

            elif option == 2:
                withdraw_amount = int(input("Please enter the amount to withdraw: "))
                if withdraw_amount > balance:
                    print("Insufficient funds.")
                else:
                    balance =balance- withdraw_amount
                    print(f"{withdraw_amount} is debited from your account")
                    print(f"Your updated balance is {balance}")

            elif option == 3:
                deposit_amount = int(input("Please enter the amount to deposit: "))
                balance =balance+ deposit_amount
                print(f"{deposit_amount} is credited to your account")
                print(f"Your updated balance is {balance}")

            elif option == 4:
                balance_transfers = int(input("Please enter the amount for transfer: "))
                if balance_transfers > balance:
                    print("Insufficient funds.")
                else:
                    balance =balance- balance_transfers
                    print(f"{balance_transfers} is debited for transfer")
                    print(f"Your updated balance is {balance}")

            elif option == 5:
                print("Exiting...")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")
else:
    print("Wrong PIN. Please try again.")
