# model.py
# Employee class for the Employee Payroll System

class Employee:
    """Represents an employee and handles payroll calculations."""

    def __init__(self, emp_id, name, department, designation,
                 basic_salary, allowances, deductions, bonus):
        """Initialize employee details."""
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.basic_salary = float(basic_salary)
        self.allowances = float(allowances)
        self.deductions = float(deductions)
        self.bonus = float(bonus)

    # ---------------- Salary Calculations ---------------- #

    def calculate_gross_salary(self):
        """Calculate and return the gross salary."""
        return self.basic_salary + self.allowances

    def calculate_net_salary(self):
        """Calculate and return the net salary."""
        gross_salary = self.calculate_gross_salary()
        return gross_salary - self.deductions + self.bonus

    # ---------------- Payslip Generation ---------------- #

    def generate_payslip(self):
        """Generate and return a formatted payslip."""
        gross_salary = self.calculate_gross_salary()
        net_salary = self.calculate_net_salary()

        payslip = f"""
        ----------------------------------------
                    EMPLOYEE PAYSLIP
        ----------------------------------------
        Employee ID   : {self.emp_id}
        Name          : {self.name}
        Department    : {self.department}
        Designation   : {self.designation}
        ----------------------------------------
        Basic Salary  : ₹{self.basic_salary:.2f}
        Allowances    : ₹{self.allowances:.2f}
        Deductions    : ₹{self.deductions:.2f}
        Bonus         : ₹{self.bonus:.2f}
        ----------------------------------------
        Gross Salary  : ₹{gross_salary:.2f}
        Net Salary    : ₹{net_salary:.2f}
        ----------------------------------------
        """
        return payslip

    # ---------------- Data Conversion Methods ---------------- #

    def to_dict(self):
        """Convert employee object to dictionary for storage."""
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "basic_salary": self.basic_salary,
            "allowances": self.allowances,
            "deductions": self.deductions,
            "bonus": self.bonus
        }

    @classmethod
    def from_dict(cls, data):
        """Create an Employee object from a dictionary."""
        return cls(
            data["emp_id"],
            data["name"],
            data["department"],
            data["designation"],
            data["basic_salary"],
            data["allowances"],
            data["deductions"],
            data["bonus"]
        )

    # ---------------- String Representation ---------------- #

    def __str__(self):
        """Return a readable string representation of the employee."""
        return (f"ID: {self.emp_id}, Name: {self.name}, "
                f"Department: {self.department}, "
                f"Designation: {self.designation}, "
                f"Net Salary: ₹{self.calculate_net_salary():.2f}")

# Testing the Employee class

# if __name__ == "__main__":
#     emp = Employee(
#         101, "Lingaraj", "IT", "Software Developer",
#         50000, 8000, 3000, 2000
#     )

#     print(emp)
#     print("\nGross Salary:", emp.calculate_gross_salary())
#     print("Net Salary:", emp.calculate_net_salary())
#     print(emp.generate_payslip())
