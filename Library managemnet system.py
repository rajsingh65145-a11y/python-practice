from abc import ABC, abstractmethod
import json
from datetime import datetime

# ---------------------------
# Utility Functions (Recursion)
# ---------------------------

def factorial(n):
    """Recursive factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Recursive fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def binary_search_recursive(arr, target, low=0, high=None):
    """Recursive binary search"""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


# ---------------------------
# Decorator Example
# ---------------------------

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# ---------------------------
# Abstract Base Class
# ---------------------------

class Item(ABC):
    def __init__(self, title, id_):
        self.title = title
        self.id = id_
        self.is_issued = False

    @abstractmethod
    def display_info(self):
        pass


# ---------------------------
# Book Class
# ---------------------------

class Book(Item):
    def __init__(self, title, author, id_):
        super().__init__(title, id_)
        self.author = author

    def display_info(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"Book: {self.title} | Author: {self.author} | Status: {status}")


# ---------------------------
# Magazine Class
# ---------------------------

class Magazine(Item):
    def __init__(self, title, issue_no, id_):
        super().__init__(title, id_)
        self.issue_no = issue_no

    def display_info(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"Magazine: {self.title} | Issue: {self.issue_no} | Status: {status}")


# ---------------------------
# User Class
# ---------------------------

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        if not item.is_issued:
            item.is_issued = True
            self.borrowed_items.append(item)
            print(f"{self.name} borrowed {item.title}")
        else:
            print(f"{item.title} is already issued!")

    def return_item(self, item):
        if item in self.borrowed_items:
            item.is_issued = False
            self.borrowed_items.remove(item)
            print(f"{self.name} returned {item.title}")
        else:
            print("Item not found in borrowed list.")

    def show_items(self):
        print(f"{self.name}'s Borrowed Items:")
        for item in self.borrowed_items:
            item.display_info()


# ---------------------------
# Library Class
# ---------------------------

class Library:
    def __init__(self):
        self.items = []

    @log_action
    def add_item(self, item):
        self.items.append(item)

    @log_action
    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]

    def display_all_items(self):
        for item in self.items:
            item.display_info()

    def search_item(self, title):
        results = [item for item in self.items if title.lower() in item.title.lower()]
        return results

    def save_to_file(self, filename="library.json"):
        data = []
        for item in self.items:
            data.append({
                "title": item.title,
                "id": item.id,
                "issued": item.is_issued
            })

        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename="library.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                print("Library loaded successfully.")
        except FileNotFoundError:
            print("No saved file found.")


# ---------------------------
# Generator Example
# ---------------------------

def id_generator():
    i = 1
    while True:
        yield i
        i += 1


# ---------------------------
# Main Execution
# ---------------------------

def main():
    library = Library()
    user = User("Harsh")

    id_gen = id_generator()

    # Adding items
    book1 = Book("Python Basics", "John Doe", next(id_gen))
    book2 = Book("Advanced Python", "Jane Smith", next(id_gen))
    mag1 = Magazine("Tech Monthly", 101, next(id_gen))

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(mag1)

    # Display items
    print("\n--- Library Items ---")
    library.display_all_items()

    # Borrow & Return
    user.borrow_item(book1)
    user.borrow_item(book1)  # Already issued
    user.show_items()

    user.return_item(book1)
    user.show_items()

    # Search
    print("\n--- Search Results ---")
    results = library.search_item("Python")
    for item in results:
        item.display_info()

    # Recursion usage
    print("\n--- Recursion Examples ---")
    print("Factorial of 5:", factorial(5))
    print("Fibonacci of 6:", fibonacci(6))

    # Binary search
    arr = [1, 3, 5, 7, 9, 11]
    print("Binary Search (7):", binary_search_recursive(arr, 7))

    # File handling
    library.save_to_file()
    library.load_from_file()

    print("\nProgram finished at:", datetime.now())


# ---------------------------
# Entry Point
# ---------------------------

if __name__ == "__main__":
    main()