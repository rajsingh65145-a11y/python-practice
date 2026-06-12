"""
Employee Management System demonstrating:
- Abstract base classes (abc)
- Static and class methods
- Property decorators with validation
- Operator overloading (__add__, __lt__, etc.)
- Data classes (simulated with dataclasses)
- Singleton pattern (Company)
- Factory method pattern
"""

from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import math


@dataclass
class Address:
    """Data class for employee address."""
    street: str
    city: str
    state: str
    zip_code: str
    
    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"


class Person(ABC):
    """Abstract base class for any person in the system."""
    
    def __init__(self, first_name: str, last_name: str, birth_date: date):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
    
    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"
    
    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self._birth_date.year - ((today.month, today.day) < (self._birth_date.month, self._birth_date.day))
    
    @abstractmethod
    def get_role(self) -> str:
        pass
    
    def __str__(self) -> str:
        return f"{self.full_name} ({self.get_role()}, {self.age} years)"


class Employee(Person):
    """Concrete employee class with salary, department, etc."""
    
    _employee_counter = 0  # class variable for generating IDs
    
    def __init__(self, first_name: str, last_name: str, birth_date: date,
                 hire_date: date, salary: float, department: str, address: Address):
        super().__init__(first_name, last_name, birth_date)
        self._employee_id = Employee._generate_employee_id()
        self._hire_date = hire_date
        self._salary = salary
        self._department = department
        self._address = address
        self._performance_reviews: List[Dict[str, Any]] = []
        self._leave_balance = 20  # days per year
        self._is_active = True
    
    @classmethod
    def _generate_employee_id(cls) -> str:
        cls._employee_counter += 1
        return f"EMP{cls._employee_counter:05d}"
    
    @property
    def employee_id(self) -> str:
        return self._employee_id
    
    @property
    def salary(self) -> float:
        return self._salary
    
    @salary.setter
    def salary(self, new_salary: float) -> None:
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        if new_salary < self._salary * 0.5:
            print(f"Warning: Salary decreased from ${self._salary:.2f} to ${new_salary:.2f}")
        self._salary = new_salary
    
    @property
    def department(self) -> str:
        return self._department
    
    @department.setter
    def department(self, new_dept: str) -> None:
        old_dept = self._department
        self._department = new_dept
        print(f"{self.full_name} moved from {old_dept} to {new_dept}")
    
    @property
    def tenure_years(self) -> float:
        delta = date.today() - self._hire_date
        return delta.days / 365.25
    
    def add_performance_review(self, reviewer: str, rating: int, comments: str) -> None:
        """Add a performance review (rating 1-5)."""
        if 1 <= rating <= 5:
            self._performance_reviews.append({
                "date": date.today().isoformat(),
                "reviewer": reviewer,
                "rating": rating,
                "comments": comments
            })
            print(f"Review added for {self.full_name}: rating {rating}/5")
        else:
            raise ValueError("Rating must be between 1 and 5")
    
    def get_average_rating(self) -> float:
        if not self._performance_reviews:
            return 0.0
        ratings = [r["rating"] for r in self._performance_reviews]
        return sum(ratings) / len(ratings)
    
    def request_leave(self, days: int) -> bool:
        if days <= self._leave_balance:
            self._leave_balance -= days
            print(f"{self.full_name} approved for {days} days leave. Remaining: {self._leave_balance}")
            return True
        else:
            print(f"Insufficient leave balance. Requested {days}, available {self._leave_balance}")
            return False
    
    def calculate_bonus(self) -> float:
        """Standard bonus = 5% of salary."""
        return self._salary * 0.05
    
    def get_role(self) -> str:
        return "Employee"
    
    def promote(self, new_salary: float, new_title: Optional[str] = None) -> None:
        self.salary = new_salary
        print(f"{self.full_name} promoted! New salary: ${self._salary:.2f}")
    
    def __lt__(self, other: 'Employee') -> bool:
        """Compare employees by salary."""
        return self._salary < other._salary
    
    def __add__(self, other: 'Employee') -> float:
        """Add two employees' salaries (useful for payroll)."""
        return self._salary + other._salary
    
    def __str__(self) -> str:
        return f"{super().__str__()} [ID: {self._employee_id}, Dept: {self._department}, Salary: ${self._salary:.2f}]"


class Manager(Employee):
    """Manager with team management and higher bonus."""
    
    def __init__(self, first_name: str, last_name: str, birth_date: date,
                 hire_date: date, salary: float, department: str, address: Address,
                 team_size: int = 0):
        super().__init__(first_name, last_name, birth_date, hire_date, salary, department, address)
        self._team_size = team_size
        self._direct_reports: List[Employee] = []
    
    def add_report(self, employee: Employee) -> None:
        self._direct_reports.append(employee)
        self._team_size = len(self._direct_reports)
        print(f"{employee.full_name} now reports to {self.full_name}")
    
    def calculate_bonus(self) -> float:
        """Manager bonus = 10% of salary + $500 per team member."""
        base_bonus = self._salary * 0.10
        team_bonus = self._team_size * 500
        return base_bonus + team_bonus
    
    def get_role(self) -> str:
        return "Manager"
    
    def __str__(self) -> str:
        return f"{super().__str__()} [Team size: {self._team_size}]"


class Developer(Employee):
    """Developer with programming language specialization."""
    
    def __init__(self, first_name: str, last_name: str, birth_date: date,
                 hire_date: date, salary: float, department: str, address: Address,
                 primary_language: str, years_experience: float):
        super().__init__(first_name, last_name, birth_date, hire_date, salary, department, address)
        self._primary_language = primary_language
        self._years_experience = years_experience
    
    @property
    def primary_language(self) -> str:
        return self._primary_language
    
    def calculate_bonus(self) -> float:
        """Developer bonus = 8% of salary + $200 per year of experience."""
        return (self._salary * 0.08) + (self._years_experience * 200)
    
    def get_role(self) -> str:
        return f"Developer ({self._primary_language})"
    
    def __str__(self) -> str:
        return f"{super().__str__()} [{self._primary_language}, {self._years_experience} yrs exp]"


class Intern(Employee):
    """Intern with lower salary and no bonus."""
    
    def __init__(self, first_name: str, last_name: str, birth_date: date,
                 hire_date: date, salary: float, department: str, address: Address,
                 school_name: str, internship_duration_months: int):
        super().__init__(first_name, last_name, birth_date, hire_date, salary, department, address)
        self._school_name = school_name
        self._duration_months = internship_duration_months
    
    def calculate_bonus(self) -> float:
        """Interns get no bonus."""
        return 0.0
    
    def get_role(self) -> str:
        return f"Intern (from {self._school_name})"


class Company:
    """Singleton class representing a company."""
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name: str):
        if not hasattr(self, '_initialized'):
            self._name = name
            self._employees: Dict[str, Employee] = {}  # emp_id -> Employee
            self._departments: Dict[str, List[Employee]] = {}
            self._initialized = True
    
    def add_employee(self, employee: Employee) -> None:
        if employee.employee_id in self._employees:
            print(f"Employee {employee.employee_id} already exists.")
            return
        self._employees[employee.employee_id] = employee
        dept = employee.department
        if dept not in self._departments:
            self._departments[dept] = []
        self._departments[dept].append(employee)
        print(f"Added {employee.full_name} to {self._name}.")
    
    def remove_employee(self, emp_id: str) -> bool:
        if emp_id in self._employees:
            emp = self._employees[emp_id]
            dept = emp.department
            self._departments[dept].remove(emp)
            del self._employees[emp_id]
            print(f"Removed {emp.full_name} from {self._name}.")
            return True
        return False
    
    def get_employee(self, emp_id: str) -> Optional[Employee]:
        return self._employees.get(emp_id)
    
    def get_all_employees(self) -> List[Employee]:
        return list(self._employees.values())
    
    def total_payroll(self) -> float:
        return sum(e.salary for e in self._employees.values())
    
    def total_bonus_payout(self) -> float:
        return sum(e.calculate_bonus() for e in self._employees.values())
    
    def get_top_performers(self, n: int = 3) -> List[Employee]:
        """Return top n employees by average performance rating."""
        rated_emps = [(e, e.get_average_rating()) for e in self._employees.values() if e.get_average_rating() > 0]
        rated_emps.sort(key=lambda x: x[1], reverse=True)
        return [emp for emp, rating in rated_emps[:n]]
    
    def department_headcount(self) -> Dict[str, int]:
        return {dept: len(emps) for dept, emps in self._departments.items()}
    
    @staticmethod
    def create_employee_from_dict(data: Dict[str, Any]) -> Employee:
        """Factory method: creates an employee from a dictionary."""
        emp_type = data.get("type")
        address = Address(**data["address"])
        birth_date = date.fromisoformat(data["birth_date"])
        hire_date = date.fromisoformat(data["hire_date"])
        
        if emp_type == "manager":
            return Manager(data["first_name"], data["last_name"], birth_date,
                          hire_date, data["salary"], data["department"], address,
                          data.get("team_size", 0))
        elif emp_type == "developer":
            return Developer(data["first_name"], data["last_name"], birth_date,
                            hire_date, data["salary"], data["department"], address,
                            data["primary_language"], data["years_experience"])
        elif emp_type == "intern":
            return Intern(data["first_name"], data["last_name"], birth_date,
                         hire_date, data["salary"], data["department"], address,
                         data["school_name"], data["internship_duration"])
        else:
            return Employee(data["first_name"], data["last_name"], birth_date,
                           hire_date, data["salary"], data["department"], address)
    
    def __len__(self) -> int:
        return len(self._employees)
    
    def __str__(self) -> str:
        return f"Company: {self._name} | Employees: {len(self._employees)} | Departments: {len(self._departments)}"


# Demonstration
if __name__ == "__main__":
    # Create addresses
    addr1 = Address("123 Main St", "New York", "NY", "10001")
    addr2 = Address("456 Oak Ave", "San Francisco", "CA", "94105")
    addr3 = Address("789 Pine Rd", "Austin", "TX", "73301")
    
    # Create employees
    alice = Manager("Alice", "Johnson", date(1985, 6, 15), date(2010, 3, 1),
                    120000, "Engineering", addr1, team_size=0)
    bob = Developer("Bob", "Smith", date(1990, 9, 22), date(2015, 7, 10),
                    95000, "Engineering", addr2, "Python", 8.5)
    carol = Developer("Carol", "Davis", date(1992, 1, 30), date(2018, 4, 20),
                      88000, "Engineering", addr2, "Java", 6.0)
    david = Intern("David", "Lee", date(2000, 11, 5), date(2024, 6, 1),
                   35000, "Engineering", addr3, "MIT", 6)
    
    # Establish reporting
    alice.add_report(bob)
    alice.add_report(carol)
    alice.add_report(david)
    
    # Add performance reviews
    alice.add_performance_review("CTO", 5, "Excellent leadership")
    bob.add_performance_review(alice.full_name, 4, "Great coding skills")
    carol.add_performance_review(alice.full_name, 5, "Exceeds expectations")
    
    # Use company singleton
    company = Company("Tech Innovators Inc.")
    company.add_employee(alice)
    company.add_employee(bob)
    company.add_employee(carol)
    company.add_employee(david)
    
    # Another reference to the same singleton
    same_company = Company("Different Name")  # Ignored, still "Tech Innovators Inc."
    print(same_company)  # Shows original name
    
    print("\n" + "="*60)
    print(company)
    print(f"Total payroll per month: ${company.total_payroll():,.2f}")
    print(f"Total bonus payout this year: ${company.total_bonus_payout():,.2f}")
    print("Department headcount:", company.department_headcount())
    
    print("\nTop performers:")
    for emp in company.get_top_performers(2):
        print(f"  {emp.full_name} (Avg rating: {emp.get_average_rating():.1f}/5)")
    
    print("\nEmployee details:")
    for emp in company.get_all_employees():
        print(emp)
        print(f"  Bonus: ${emp.calculate_bonus():,.2f}")
        print(f"  Leave balance: {emp._leave_balance} days")
    
    # Operator overloading demo
    print("\nSalary comparison (Bob < Carol?):", bob < carol)
    print(f"Sum of Bob and Carol's salaries: ${bob + carol:,.2f}")
    
    # Factory method
    new_emp_data = {
        "type": "developer",
        "first_name": "Eve",
        "last_name": "Brown",
        "birth_date": "1995-04-12",
        "hire_date": "2023-01-15",
        "salary": 82000,
        "department": "Engineering",
        "address": {
            "street": "321 Cedar St",
            "city": "Seattle",
            "state": "WA",
            "zip_code": "98101"
        },
        "primary_language": "JavaScript",
        "years_experience": 4.5
    }
    eve = Company.create_employee_from_dict(new_emp_data)
    company.add_employee(eve)
    
    print(f"\nTotal employees after adding Eve: {len(company)}")