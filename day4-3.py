class BankAccount:

    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
            print("New balance:", self.balance)
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print("New balance:", self.balance)

    def check_balance(self):
        print("Current balance:", self.balance)

    def show_account(self):
        print("------------------------")
        print("Account Information")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("------------------------")


account = BankAccount("Ali", "123456", 1000)


while True:

    print()
    print("========================")
    print("       MINI BANK")
    print("========================")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Account Information")
    print("5. Exit")
    print("========================")

    choice = input("Choose an option: ")

    if choice == "1":
        account.check_balance()

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "4":
        account.show_account()

    elif choice == "5":
        print("Thank you for using Mini Bank.")
        break

    else:
        print("Invalid option. Please choose 1-5.")