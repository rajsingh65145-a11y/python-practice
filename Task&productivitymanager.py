from abc import ABC, abstractmethod
import json
from datetime import datetime

# ---------------------------
# Recursion Utilities
# ---------------------------

def count_completed(tasks, n):
    """Recursive count of completed tasks"""
    if n == 0:
        return 0
    return (1 if tasks[n-1].completed else 0) + count_completed(tasks, n-1)


def total_priority(tasks, n):
    """Recursive sum of priorities"""
    if n == 0:
        return 0
    return tasks[n-1].priority + total_priority(tasks, n-1)


# ---------------------------
# Decorator
# ---------------------------

def action_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[ACTION] {func.__name__} executed")
        return func(*args, **kwargs)
    return wrapper


# ---------------------------
# Custom Exception
# ---------------------------

class TaskError(Exception):
    pass


# ---------------------------
# Abstract Task Class
# ---------------------------

class Task(ABC):
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    @abstractmethod
    def show(self):
        pass

    def mark_done(self):
        self.completed = True


# ---------------------------
# Work Task
# ---------------------------

class WorkTask(Task):
    def __init__(self, title, priority, deadline):
        super().__init__(title, priority)
        self.deadline = deadline

    def show(self):
        status = "Done" if self.completed else "Pending"
        print(f"[Work] {self.title} | Priority: {self.priority} | Deadline: {self.deadline} | {status}")


# ---------------------------
# Personal Task
# ---------------------------

class PersonalTask(Task):
    def __init__(self, title, priority):
        super().__init__(title, priority)

    def show(self):
        status = "Done" if self.completed else "Pending"
        print(f"[Personal] {self.title} | Priority: {self.priority} | {status}")


# ---------------------------
# Manager Class
# ---------------------------

class TaskManager:
    def __init__(self):
        self.tasks = []

    @action_logger
    def add_task(self, task):
        self.tasks.append(task)

    @action_logger
    def remove_task(self, title):
        self.tasks = [t for t in self.tasks if t.title != title]

    def show_all(self):
        for task in self.tasks:
            task.show()

    def find_task(self, title):
        for t in self.tasks:
            if t.title == title:
                return t
        return None

    def save(self, filename="tasks.json"):
        data = []
        for t in self.tasks:
            data.append({
                "title": t.title,
                "priority": t.priority,
                "completed": t.completed
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def load(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                print("Tasks loaded")
        except FileNotFoundError:
            print("No saved tasks found")


# ---------------------------
# Generator
# ---------------------------

def task_id_generator():
    i = 1
    while True:
        yield f"TASK-{i}"
        i += 1


# ---------------------------
# Productivity Calculator
# ---------------------------

class Productivity:
    def __init__(self, tasks):
        self.tasks = tasks

    def completion_rate(self):
        if not self.tasks:
            return 0
        completed = count_completed(self.tasks, len(self.tasks))
        return (completed / len(self.tasks)) * 100

    def average_priority(self):
        if not self.tasks:
            return 0
        total = total_priority(self.tasks, len(self.tasks))
        return total / len(self.tasks)


# ---------------------------
# Main Function
# ---------------------------

def main():
    manager = TaskManager()
    id_gen = task_id_generator()

    # Create tasks
    t1 = WorkTask(f"{next(id_gen)} - Finish project", 5, "2026-06-01")
    t2 = PersonalTask(f"{next(id_gen)} - Gym", 3)
    t3 = WorkTask(f"{next(id_gen)} - Study Python", 4, "2026-05-10")

    manager.add_task(t1)
    manager.add_task(t2)
    manager.add_task(t3)

    # Mark some tasks
    t1.mark_done()
    t2.mark_done()

    # Show tasks
    print("\n--- All Tasks ---")
    manager.show_all()

    # Productivity stats
    stats = Productivity(manager.tasks)
    print("\nCompletion Rate:", stats.completion_rate(), "%")
    print("Average Priority:", stats.average_priority())

    # Error handling
    try:
        task = manager.find_task("Nonexistent Task")
        if task is None:
            raise TaskError("Task not found!")
    except TaskError as e:
        print("Error:", e)

    # Save & Load
    manager.save()
    manager.load()

    print("\nCompleted at:", datetime.now())


# ---------------------------
# Entry Point
# ---------------------------

if __name__ == "__main__":
    main()