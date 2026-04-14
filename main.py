# main.py
# Menu-Driven Interface for Employee Payroll System

from model import Employee
from service import PayrollService


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("        EMPLOYEE PAYROLL SYSTEM")
    print("=" * 50)
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee Details")
    print("4. Delete Employee")
    print("5. Calculate Salary")
    print("6. Generate Payslip")
    print("7. Exit")
    print("=" * 50)


def get_float_input(prompt):
    """Safely get numeric input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_int_input(prompt):
    """Safely get integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def add_employee(service):
    """Add a new employee."""
    try:
        emp_id = get_int_input("Enter Employee ID: ")
        name = input("Enter Name: ").strip()
        department = input("Enter Department: ").strip()
        designation = input("Enter Designation: ").strip()

        if not name or not department or not designation:
            print("Fields cannot be empty.")
            return

        basic_salary = get_float_input("Enter Basic Salary: ")
        allowances = get_float_input("Enter Allowances: ")
        deductions = get_float_input("Enter Deductions: ")
        bonus = get_float_input("Enter Bonus: ")

        employee = Employee(
            emp_id, name, department, designation,
            basic_salary, allowances, deductions, bonus
        )

        print(service.add_employee(employee))

    except ValueError as e:
        print("Error:", e)


def view_employees(service):
    """Display all employees."""
    employees = service.view_employees()
    if not employees:
        print("No employee records found.")
        return

    print("\nEmployee Records:")
    print("-" * 70)
    for emp in employees:
        print(emp)


def update_employee(service):
    """Update employee details."""
    try:
        emp_id = get_int_input("Enter Employee ID to Update: ")
        emp = service.search_employee(emp_id)

        print("\nLeave fields blank to keep existing values.")

        name = input(f"Enter Name ({emp.name}): ").strip() or emp.name
        department = input(f"Enter Department ({emp.department}): ").strip() or emp.department
        designation = input(f"Enter Designation ({emp.designation}): ").strip() or emp.designation

        def optional_float(prompt, default):
            value = input(f"{prompt} ({default}): ").strip()
            return float(value) if value else default

        basic_salary = optional_float("Enter Basic Salary", emp.basic_salary)
        allowances = optional_float("Enter Allowances", emp.allowances)
        deductions = optional_float("Enter Deductions", emp.deductions)
        bonus = optional_float("Enter Bonus", emp.bonus)

        print(service.update_employee(
            emp_id,
            name=name,
            department=department,
            designation=designation,
            basic_salary=basic_salary,
            allowances=allowances,
            deductions=deductions,
            bonus=bonus
        ))

    except ValueError as e:
        print("Error:", e)


def delete_employee(service):
    """Delete an employee."""
    try:
        emp_id = get_int_input("Enter Employee ID to Delete: ")
        print(service.delete_employee(emp_id))
    except ValueError as e:
        print("Error:", e)


def calculate_salary(service):
    """Calculate salary for an employee."""
    try:
        emp_id = get_int_input("Enter Employee ID: ")
        salary = service.calculate_salary(emp_id)

        print("\nSalary Details:")
        print(f"Gross Salary: ₹{salary['gross_salary']:.2f}")
        print(f"Net Salary  : ₹{salary['net_salary']:.2f}")

    except ValueError as e:
        print("Error:", e)


def generate_payslip(service):
    """Generate employee payslip."""
    try:
        emp_id = get_int_input("Enter Employee ID: ")
        payslip = service.generate_payslip(emp_id)
        print(payslip)
    except ValueError as e:
        print("Error:", e)


def main():
    """Main function to run the payroll system."""
    service = PayrollService()

    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_employee(service)
        elif choice == "2":
            view_employees(service)
        elif choice == "3":
            update_employee(service)
        elif choice == "4":
            delete_employee(service)
        elif choice == "5":
            calculate_salary(service)
        elif choice == "6":
            generate_payslip(service)
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 7.")


# Program Entry Point
if __name__ == "__main__":
    main()
