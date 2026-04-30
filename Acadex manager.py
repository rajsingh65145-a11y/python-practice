from abc import ABC, abstractmethod
import json
from datetime import datetime

# ---------------------------
# Recursion Utilities
# ---------------------------

def sum_of_digits(n):
    """Recursive sum of digits"""
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def power(base, exp):
    """Recursive power function"""
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def recursive_max(arr, n):
    """Find max using recursion"""
    if n == 1:
        return arr[0]
    return max(arr[n-1], recursive_max(arr, n-1))


# ---------------------------
# Decorator
# ---------------------------

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# ---------------------------
# Abstract Base Class
# ---------------------------

class Person(ABC):
    def __init__(self, name, id_):
        self.name = name
        self.id = id_

    @abstractmethod
    def display(self):
        pass


# ---------------------------
# Student Class
# ---------------------------

class Student(Person):
    def __init__(self, name, id_):
        super().__init__(name, id_)
        self.courses = {}
    
    def enroll(self, course):
        self.courses[course.name] = None
        print(f"{self.name} enrolled in {course.name}")

    def add_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
        else:
            print("Course not found!")

    def calculate_average(self):
        grades = [g for g in self.courses.values() if g is not None]
        if not grades:
            return 0
        return sum(grades) / len(grades)

    def display(self):
        print(f"Student: {self.name} | ID: {self.id}")
        for course, grade in self.courses.items():
            print(f"  {course}: {grade}")


# ---------------------------
# Course Class
# ---------------------------

class Course:
    def __init__(self, name):
        self.name = name


# ---------------------------
# Management System
# ---------------------------

class StudentSystem:
    def __init__(self):
        self.students = []

    @logger
    def add_student(self, student):
        self.students.append(student)

    def find_student(self, id_):
        for s in self.students:
            if s.id == id_:
                return s
        return None

    def display_all(self):
        for s in self.students:
            s.display()

    def save(self, filename="students.json"):
        data = []
        for s in self.students:
            data.append({
                "name": s.name,
                "id": s.id,
                "courses": s.courses
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def load(self, filename="students.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                print("Data loaded successfully")
        except FileNotFoundError:
            print("File not found!")


# ---------------------------
# Generator
# ---------------------------

def student_id_generator():
    i = 100
    while True:
        yield i
        i += 1


# ---------------------------
# Custom Exception
# ---------------------------

class InvalidGradeError(Exception):
    pass


# ---------------------------
# Main Function
# ---------------------------

def main():
    system = StudentSystem()
    id_gen = student_id_generator()

    # Create students
    s1 = Student("Harsh", next(id_gen))
    s2 = Student("Ravi", next(id_gen))

    system.add_student(s1)
    system.add_student(s2)

    # Create courses
    c1 = Course("Math")
    c2 = Course("Science")

    # Enroll
    s1.enroll(c1)
    s1.enroll(c2)

    s2.enroll(c1)

    # Add grades with error handling
    try:
        grade = 85
        if grade < 0 or grade > 100:
            raise InvalidGradeError("Invalid grade value!")
        s1.add_grade("Math", grade)
    except InvalidGradeError as e:
        print(e)

    s1.add_grade("Science", 90)
    s2.add_grade("Math", 75)

    # Display
    print("\n--- Student Data ---")
    system.display_all()

    # Average
    print("\nAverage of Harsh:", s1.calculate_average())

    # Recursion examples
    print("\n--- Recursion ---")
    print("Sum of digits (1234):", sum_of_digits(1234))
    print("2^5:", power(2, 5))
    print("Max element:", recursive_max([3, 7, 2, 9, 5], 5))

    # Save/Load
    system.save()
    system.load()

    print("\nCompleted at:", datetime.now())


# ---------------------------
# Entry Point
# ---------------------------

if __name__ == "__main__":
    main()