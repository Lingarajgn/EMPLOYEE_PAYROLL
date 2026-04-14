# service.py
# Business logic for the Employee Payroll System

import json
from model import Employee


class PayrollService:
    """Handles CRUD operations and payroll processing."""

    def __init__(self, filename="data.txt"):
        self.filename = filename
        self.employees = {}
        self.load_from_file()

    # ---------------- File Handling ---------------- #

    def load_from_file(self):
        """Load employee data from file."""
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for emp_id, emp_data in data.items():
                    self.employees[int(emp_id)] = Employee.from_dict(emp_data)
        except FileNotFoundError:
            self.employees = {}
        except json.JSONDecodeError:
            self.employees = {}

    def save_to_file(self):
        """Save employee data to file."""
        data = {
            emp_id: emp.to_dict()
            for emp_id, emp in self.employees.items()
        }
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # ---------------- CRUD Operations ---------------- #

    def add_employee(self, employee):
        """Add a new employee."""
        if employee.emp_id in self.employees:
            raise ValueError("Employee ID already exists.")
        self.employees[employee.emp_id] = employee
        self.save_to_file()
        return "Employee added successfully."

    def view_employees(self):
        """Return all employee records."""
        return list(self.employees.values())

    def search_employee(self, emp_id):
        """Search for an employee by ID."""
        if emp_id not in self.employees:
            raise ValueError("Employee not found.")
        return self.employees[emp_id]

    def update_employee(self, emp_id, **kwargs):
        """Update employee details."""
        if emp_id not in self.employees:
            raise ValueError("Employee not found.")

        emp = self.employees[emp_id]

        for key, value in kwargs.items():
            if hasattr(emp, key) and value is not None:
                if key in ["basic_salary", "allowances", "deductions", "bonus"]:
                    setattr(emp, key, float(value))
                else:
                    setattr(emp, key, value)

        self.save_to_file()
        return "Employee updated successfully."

    def delete_employee(self, emp_id):
        """Delete an employee."""
        if emp_id not in self.employees:
            raise ValueError("Employee not found.")

        del self.employees[emp_id]
        self.save_to_file()
        return "Employee deleted successfully."

    # ---------------- Payroll Operations ---------------- #

    def calculate_salary(self, emp_id):
        """Calculate salary details for an employee."""
        emp = self.search_employee(emp_id)
        return {
            "gross_salary": emp.calculate_gross_salary(),
            "net_salary": emp.calculate_net_salary()
        }

    def generate_payslip(self, emp_id):
        """Generate payslip for an employee."""
        emp = self.search_employee(emp_id)
        return emp.generate_payslip()


#testing part:

# if __name__ == "__main__":
#     service = PayrollService()

#     try:
#         # Add an employee
#         emp = Employee(
#             101, "Lingaraj", "IT", "Developer",
#             50000, 8000, 3000, 2000
#         )
#         print(service.add_employee(emp))
#     except ValueError as e:
#         print(e)

#     # View employees
#     print("\nEmployee Records:")
#     for emp in service.view_employees():
#         print(emp)

#     # Generate payslip
#     try:
#         print("\nGenerated Payslip:")
#         print(service.generate_payslip(101))
#     except ValueError as e:
#         print(e)
