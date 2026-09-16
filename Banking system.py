from abc import ABC, abstractmethod
import json
from datetime import datetime

# ---------------------------
# Recursion Utilities
# ---------------------------

def compound_interest(principal, rate, time):
    """Recursive compound interest calculation"""
    if time == 0:
        return principal
    return compound_interest(principal * (1 + rate), rate, time - 1)


def sum_transactions(transactions, n):
    """Recursive sum of transactions"""
    if n == 0:
        return 0
    return transactions[n-1] + sum_transactions(transactions, n-1)


# ---------------------------
# Decorator
# ---------------------------

def transaction_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[TRANSACTION] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper


# ---------------------------
# Custom Exception
# ---------------------------

class InsufficientBalanceError(Exception):
    pass


# ---------------------------
# Abstract Account Class
# ---------------------------

class Account(ABC):
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.transactions = []

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance!")
        self.balance -= amount
        self.transactions.append(-amount)

    def show_balance(self):
        print(f"{self.name}'s Balance: ₹{self.balance}")

    def show_transactions(self):
        print("Transactions:", self.transactions)


# ---------------------------
# Savings Account
# ---------------------------

class SavingsAccount(Account):
    def __init__(self, name, acc_no, balance=0):
        super().__init__(name, acc_no, balance)

    def account_type(self):
        return "Savings"

    def add_interest(self, rate, time):
        self.balance = compound_interest(self.balance, rate, time)


# ---------------------------
# Current Account
# ---------------------------

class CurrentAccount(Account):
    def __init__(self, name, acc_no, balance=0):
        super().__init__(name, acc_no, balance)

    def account_type(self):
        return "Current"


# ---------------------------
# Bank System
# ---------------------------

class Bank:
    def __init__(self):
        self.accounts = []

    @transaction_logger
    def create_account(self, account):
        self.accounts.append(account)

    def find_account(self, acc_no):
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                return acc
        return None

    def display_all_accounts(self):
        for acc in self.accounts:
            print(f"{acc.name} | {acc.acc_no} | {acc.account_type()} | ₹{acc.balance}")

    def save(self, filename="bank.json"):
        data = []
        for acc in self.accounts:
            data.append({
                "name": acc.name,
                "acc_no": acc.acc_no,
                "balance": acc.balance
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def load(self, filename="bank.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                print("Bank data loaded")
        except FileNotFoundError:
            print("No file found!")


# ---------------------------
# Generator
# ---------------------------

def account_number_generator():
    num = 1000
    while True:
        yield num
        num += 1


# ---------------------------
# Main Function
# ---------------------------

def main():
    bank = Bank()
    acc_gen = account_number_generator()

    # Create accounts
    acc1 = SavingsAccount("Harsh", next(acc_gen), 5000)
    acc2 = CurrentAccount("Ravi", next(acc_gen), 10000)

    bank.create_account(acc1)
    bank.create_account(acc2)

    # Transactions
    try:
        acc1.deposit(2000)
        acc1.withdraw(1000)
        acc1.withdraw(10000)  # error
    except InsufficientBalanceError as e:
        print("Error:", e)

    acc2.deposit(5000)

    # Interest
    acc1.add_interest(0.05, 2)

    # Display
    print("\n--- Account Details ---")
    bank.display_all_accounts()

    acc1.show_transactions()

    # Recursion usage
    print("\nTotal Transactions:", sum_transactions(acc1.transactions, len(acc1.transactions)))

    # Save/Load
    bank.save()
    bank.load()

    print("\nFinished at:", datetime.now())


# ---------------------------
# Entry Point
# ---------------------------

if __name__ == "__main__":
    main()