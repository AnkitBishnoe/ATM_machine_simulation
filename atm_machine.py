"""
ATM Machine Simulation
A simple ATM machine simulator with features to check balance, withdraw money, and deposit money.
"""

class ATMMachine:
    def __init__(self, initial_balance=5000):
        """Initialize ATM machine with initial balance"""
        self.balance = initial_balance
        self.transaction_history = []
        self.pin = "1234"  # Default PIN
        self.logged_in = False
        
    def verify_pin(self, entered_pin):
        """Verify the PIN entered by user"""
        if entered_pin == self.pin:
            self.logged_in = True
            print("✓ PIN verified! You are now logged in.")
            return True
        else:
            print("✗ Invalid PIN. Access denied.")
            return False
    
    def check_balance(self):
        """Check current balance"""
        if not self.logged_in:
            print("✗ Please log in first.")
            return
        
        print(f"\n{'='*40}")
        print(f"Current Balance: Rs. {self.balance:,.2f}")
        print(f"{'='*40}\n")
        self.transaction_history.append(f"Balance Check: Rs. {self.balance}")
    
    def withdraw_money(self, amount):
        """Withdraw money from the account"""
        if not self.logged_in:
            print("✗ Please log in first.")
            return False
        
        # Validation checks
        if amount <= 0:
            print("✗ Withdrawal amount must be greater than zero.")
            return False
        
        if amount > self.balance:
            print(f"✗ Insufficient balance! Your balance is: Rs. {self.balance:,.2f}")
            return False
        
        if amount % 100 != 0:
            print("✗ Amount should be in multiples of 100.")
            return False
        
        # Process withdrawal
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -Rs. {amount} | Balance: Rs. {self.balance}")
        
        print(f"\n{'='*40}")
        print(f"✓ Withdrawal Successful!")
        print(f"Amount Withdrawn: Rs. {amount:,.2f}")
        print(f"Remaining Balance: Rs. {self.balance:,.2f}")
        print(f"{'='*40}\n")
        
        return True
    
    def deposit_money(self, amount):
        """Deposit money into the account"""
        if not self.logged_in:
            print("✗ Please log in first.")
            return False
        
        # Validation checks
        if amount <= 0:
            print("✗ Deposit amount must be greater than zero.")
            return False
        
        if amount % 100 != 0:
            print("✗ Amount should be in multiples of 100.")
            return False
        
        # Process deposit
        self.balance += amount
        self.transaction_history.append(f"Deposit: +Rs. {amount} | Balance: Rs. {self.balance}")
        
        print(f"\n{'='*40}")
        print(f"✓ Deposit Successful!")
        print(f"Amount Deposited: Rs. {amount:,.2f}")
        print(f"New Balance: Rs. {self.balance:,.2f}")
        print(f"{'='*40}\n")
        
        return True
    
    def view_transaction_history(self):
        """View all transaction history"""
        if not self.logged_in:
            print("✗ Please log in first.")
            return
        
        print(f"\n{'='*40}")
        print("TRANSACTION HISTORY")
        print(f"{'='*40}")
        
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for i, transaction in enumerate(self.transaction_history, 1):
                print(f"{i}. {transaction}")
        
        print(f"{'='*40}\n")
    
    def logout(self):
        """Logout from ATM"""
        if self.logged_in:
            self.logged_in = False
            print("✓ You have been logged out successfully.")
        else:
            print("✗ You are not logged in.")
    
    def change_pin(self, old_pin, new_pin):
        """Change the PIN"""
        if not self.logged_in:
            print("✗ Please log in first.")
            return False
        
        if old_pin != self.pin:
            print("✗ Old PIN is incorrect.")
            return False
        
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("✗ PIN must be 4 digits.")
            return False
        
        self.pin = new_pin
        print("✓ PIN changed successfully!")
        return True


def main():
    """Main function to run the ATM simulation"""
    atm = ATMMachine(initial_balance=5000)
    
    print("\n" + "="*50)
    print("WELCOME TO ATM MACHINE SIMULATION")
    print("="*50)
    print(f"Initial Balance: Rs. 5000")
    print(f"Default PIN: 1234")
    print("="*50 + "\n")
    
    while True:
        # Login system
        if not atm.logged_in:
            print("\n--- LOGIN ---")
            entered_pin = input("Enter your PIN (or 'q' to quit): ")
            
            if entered_pin.lower() == 'q':
                print("\n✓ Thank you for using ATM Machine. Goodbye!")
                break
            
            if not entered_pin.isdigit() or len(entered_pin) != 4:
                print("✗ PIN must be 4 digits.")
                continue
            
            atm.verify_pin(entered_pin)
            continue
        
        # Main menu
        print("\n" + "-"*40)
        print("MAIN MENU")
        print("-"*40)
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. View Transaction History")
        print("5. Change PIN")
        print("6. Logout")
        print("7. Exit")
        print("-"*40)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            atm.check_balance()
        
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: Rs. "))
                atm.withdraw_money(amount)
            except ValueError:
                print("✗ Please enter a valid amount.")
        
        elif choice == '3':
            try:
                amount = float(input("Enter amount to deposit: Rs. "))
                atm.deposit_money(amount)
            except ValueError:
                print("✗ Please enter a valid amount.")
        
        elif choice == '4':
            atm.view_transaction_history()
        
        elif choice == '5':
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN (4 digits): ")
            atm.change_pin(old_pin, new_pin)
        
        elif choice == '6':
            atm.logout()
        
        elif choice == '7':
            print("\n✓ Thank you for using ATM Machine. Goodbye!")
            break
        
        else:
            print("✗ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
