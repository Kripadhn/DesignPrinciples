class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1

class EmployeeDB:
    def save_to_database(self, employee):
        # code to save employee to the database
        pass
