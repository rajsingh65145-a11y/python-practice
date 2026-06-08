"""
Banking System demonstrating:
- Encapsulation (private attributes, getters/setters)
- Inheritance (SavingsAccount, CurrentAccount inherit Account)
- Polymorphism (overridden methods)
- Class methods and static methods
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional


class Account(ABC):
    """Abstract base class for all account types."""
    
    _last_account_number = 1000  # Class variable for generating account numbers
    
    def __init__(self, holder_name: str, initial_balance: float = 0.0):
        self._holder_name = holder_name
        self._balance = initial_balance
        self._account_number = Account._generate_account_number()
        self._transactions: List[str] = []
        self._is_active = True
        self._created_date = datetime.now()
        
        if initial_balance > 0:
            self._add_transaction(f"Initial deposit: ${initial_balance:.2f}")
    
    @classmethod
    def _generate_account_number(cls) -> int:
        cls._last_account_number += 1
        return cls._last_account_number
    
    @property
    def holder_name(self) -> str:
        return self._holder_name
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def account_number(self) -> int:
        return self._account_number
    
    @property
    def is_active(self) -> bool:
        return self._is_active
    
    def _add_transaction(self, description: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transactions.append(f"[{timestamp}] {description}")
    
    def deposit(self, amount: float) -> bool:
        """Deposit money into the account."""
        if not self._is_active:
            print("Cannot deposit: Account is closed.")
            return False
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        
        self._balance += amount
        self._add_transaction(f"Deposited: ${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money (to be implemented by subclasses with their rules)."""
        if not self._is_active:
            print("Cannot withdraw: Account is closed.")
            return False
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if self._balance >= amount:
            self._balance -= amount
            self._add_transaction(f"Withdrew: ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False
    
    @abstractmethod
    def calculate_interest(self) -> float:
        """Calculate interest for the account (if any)."""
        pass
    
    def close_account(self) -> None:
        """Close the account and prevent further transactions."""
        self._is_active = False
        self._add_transaction("Account closed.")
        print(f"Account {self._account_number} closed.")
    
    def get_statement(self) -> None:
        """Print transaction history."""
        print(f"\n--- Statement for Account {self._account_number} ({self._holder_name}) ---")
        print(f"Created: {self._created_date.strftime('%Y-%m-%d')}")
        print(f"Current Balance: ${self._balance:.2f}")
        print("Transactions:")
        for trans in self._transactions:
            print(f"  {trans}")
        print("--------------------------------------------------\n")
    
    def __str__(self) -> str:
        return f"Account[{self._account_number}]: {self._holder_name}, Balance=${self._balance:.2f}"


class SavingsAccount(Account):
    """Savings account with interest rate and minimum balance requirement."""
    
    INTEREST_RATE = 0.03  # 3% annual interest
    MINIMUM_BALANCE = 500.0
    
    def __init__(self, holder_name: str, initial_balance: float = 0.0):
        super().__init__(holder_name, initial_balance)
        if initial_balance < self.MINIMUM_BALANCE:
            print(f"Warning: Savings account requires minimum balance of ${self.MINIMUM_BALANCE:.2f}")
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw with penalty if balance falls below minimum."""
        if not self._is_active:
            return False
        
        # Check if after withdrawal balance would be below minimum
        if self._balance - amount < self.MINIMUM_BALANCE:
            penalty = 25.0
            print(f"Withdrawal would drop below ${self.MINIMUM_BALANCE:.2f}. Applying ${penalty:.2f} penalty.")
            amount += penalty
        
        return super().withdraw(amount)
    
    def calculate_interest(self) -> float:
        """Calculate interest based on current balance."""
        interest = self._balance * self.INTEREST_RATE
        return interest
    
    def apply_interest(self) -> None:
        """Apply annual interest to the account."""
        interest = self.calculate_interest()
        if interest > 0:
            self._balance += interest
            self._add_transaction(f"Interest credited: ${interest:.2f} (rate {self.INTEREST_RATE*100}%)")
            print(f"Interest of ${interest:.2f} applied. New balance: ${self._balance:.2f}")


class CurrentAccount(Account):
    """Current account with overdraft facility."""
    
    OVERDRAFT_LIMIT = 1000.0
    
    def __init__(self, holder_name: str, initial_balance: float = 0.0):
        super().__init__(holder_name, initial_balance)
        self._overdraft_used = 0.0
    
    def withdraw(self, amount: float) -> bool:
        """Allow withdrawal up to overdraft limit."""
        if not self._is_active:
            return False
        
        available_funds = self._balance + (self.OVERDRAFT_LIMIT - self._overdraft_used)
        if amount <= available_funds:
            if amount <= self._balance:
                self._balance -= amount
            else:
                # Use overdraft
                remaining = amount - self._balance
                self._balance = 0
                self._overdraft_used += remaining
            
            self._add_transaction(f"Withdrew: ${amount:.2f} (Overdraft used: ${self._overdraft_used:.2f})")
            print(f"Withdrew ${amount:.2f}. Balance: ${self._balance:.2f}, Overdraft used: ${self._overdraft_used:.2f}")
            return True
        else:
            print(f"Overdraft limit exceeded. Available: ${available_funds:.2f}")
            return False
    
    def calculate_interest(self) -> float:
        """Current accounts do not earn interest."""
        return 0.0
    
    def get_overdraft_remaining(self) -> float:
        return self.OVERDRAFT_LIMIT - self._overdraft_used


class Bank:
    """Bank that manages multiple accounts."""
    
    def __init__(self, name: str):
        self._name = name
        self._accounts: List[Account] = []
    
    def add_account(self, account: Account) -> None:
        self._accounts.append(account)
        print(f"Account {account.account_number} ({account.holder_name}) added to {self._name}.")
    
    def get_account(self, account_number: int) -> Optional[Account]:
        for acc in self._accounts:
            if acc.account_number == account_number:
                return acc
        print(f"Account {account_number} not found.")
        return None
    
    def total_balance(self) -> float:
        return sum(acc.balance for acc in self._accounts if acc.is_active)
    
    def apply_interest_to_all(self) -> None:
        for acc in self._accounts:
            if isinstance(acc, SavingsAccount) and acc.is_active:
                acc.apply_interest()
    
    def display_all_accounts(self) -> None:
        print(f"\n=== {self._name} - All Accounts ===")
        for acc in self._accounts:
            print(acc)
        print(f"Total Bank Balance: ${self.total_balance():.2f}\n")


# Demonstration
if __name__ == "__main__":
    # Create a bank
    my_bank = Bank("First Python Bank")
    
    # Create accounts
    alice_savings = SavingsAccount("Alice Johnson", 1000.0)
    bob_current = CurrentAccount("Bob Smith", 200.0)
    charlie_savings = SavingsAccount("Charlie Brown", 600.0)
    
    # Add accounts to bank
    my_bank.add_account(alice_savings)
    my_bank.add_account(bob_current)
    my_bank.add_account(charlie_savings)
    
    # Perform transactions
    alice_savings.deposit(500)
    alice_savings.withdraw(200)
    alice_savings.withdraw(900)  # This triggers penalty
    
    bob_current.withdraw(300)    # Uses overdraft
    bob_current.deposit(150)
    
    # Apply interest to savings accounts
    my_bank.apply_interest_to_all()
    
    # Print statements
    alice_savings.get_statement()
    bob_current.get_statement()
    
    # Display all accounts
    my_bank.display_all_accounts()
    
    # Close an account
    charlie_savings.close_account()
    charlie_savings.deposit(50)  # Should fail