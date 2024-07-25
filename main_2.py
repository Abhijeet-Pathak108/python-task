import time
from datetime import date

class ATM:
    today = date.today()
    format_time = time.localtime()
    current_time = time.strftime("%H:%M:%S", format_time)
    
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.transaction = []
        
    def check_pin(self):
        enter_pin = int(input("Please enter your account pin number: "))
        print(' ')
        if enter_pin == self.pin:
            return True
        else:
            print("Entered pin is incorrect! Please enter your correct pin\n")
            return False
        
    def balance_inquiry(self):
        if self.check_pin():
            print(f"Your current balance is: {self.balance}")
            print("")
            transaction = f"Balance inquiry on {self.today} at {self.current_time}, current balance is: {self.balance}"
            self.transaction.append(transaction)
            self.write_transaction(transaction)
            
    def cash_withdrawal(self):
        if self.check_pin():
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Your account has been debited by {amount}")
                print(f"Your current balance is {self.balance}")
                transaction = f"Balance withdrawal on {self.today} at {self.current_time}, current balance is: {self.balance}"
                self.transaction.append(transaction)
                self.write_transaction(transaction)
            else:
                print("Insufficient balance")
                
    def cash_deposit(self):
        if self.check_pin():
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print("Your current balance is:", self.balance)
            transaction = f"Amount deposit on {self.today} at {self.current_time}, current balance is: {self.balance}"
            self.transaction.append(transaction)
            self.write_transaction(transaction)
            
    def pin_change(self):
        if self.check_pin():
            new_pin = int(input("Enter your new pin: "))
            confirm_pin = int(input("Confirm your new pin: "))
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("Your pin changed successfully")
                transaction = f"Pin change on {self.today} at {self.current_time}"
                self.transaction.append(transaction)
                self.write_transaction(transaction)
            else:
                print("Confirm pin and new pin do not match")
                
    def transaction_history(self):
        if self.check_pin():
            print("Transaction history:")
            for count, t in enumerate(self.transaction):
                print(count, t)
            with open("transaction_history.txt", "w") as file:
                for t in self.transaction:
                    file.write(t + "\n")
            print("Transaction history has been saved to transaction_history.txt")
    
    def write_transaction(self, transaction):
        with open("transaction_history.txt", "a") as file:
            file.write(transaction + "\n")
    
def main():
        atm = ATM(1111, 10000)
        print("Please! Insert your card......\n")
        time.sleep(5)
        print("Your card is under process! Do not remove it.....\n")
        time.sleep(3)
        print("Your card has been processed successfully!!!\n")
        while True:
            time.sleep(2)
            print("Please select what you want to use....\n")
            print('''1. Balance inquiry
    2. Cash withdrawal
    3. Cash deposit
    4. Pin change
    5. Transaction history
    6. Exit''')
            choice = int(input("Choose any one option: "))
            match choice:
                case 1:
                    atm.balance_inquiry()
                case 2:
                    atm.cash_withdrawal()
                case 3:
                    atm.cash_deposit()
                case 4:
                    atm.pin_change()
                case 5:
                    atm.transaction_history()
                case 6:
                    time.sleep(1)
                    print("Thank you for using our ATM")
                    break
                case _:
                    print('Please choose a valid option')
  
    
main()

