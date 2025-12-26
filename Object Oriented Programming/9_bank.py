class bankAccount:
    account_number = 0
    owner_name = ""
    balance = 0.0

    def __init__(self, acc_num, owner, bal):
        self.account_number = acc_num
        self.owner_name = owner
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

    def check_balance(self):
        print(f"Current balance is {self.balance}")


b1 = bankAccount(123456, "Umar", 1000.0)
b1.deposit(500.0)
b1.withdraw(200.0)
b1.check_balance()