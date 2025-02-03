
class Employee:
    '''Class to check employee information'''
    def __init__(self, id, name, salary, deptt):
        self.set_emp_id(id)    # Employee ID
        self.set_emp_name(name)    # Employee Name
        self.set_emp_salary(salary)    # Employee Salary
        self.set_department(deptt)     # Employee Department

    # Setter Methods:
    def set_emp_id(self, id):
        '''Set Employee ID'''
        self.emp_id = id
    def set_emp_name(self, name):
        '''Set Employee Name'''
        self.emp_name = name
    def set_emp_salary(self, salary):
        '''Set Employee Salary'''
        self.emp_salary = salary
    def set_department(self, deptt):
        '''Set Employee Department'''
        self.department = deptt

    # Getter Methods:
    def get_emp_id(self):
        '''Get Employee ID'''
        return self.emp_id
    def get_emp_name(self):
        '''Get Employee Name'''
        return self.emp_name
    def get_emp_salary(self):
        '''Get Employee Salary'''
        return self.emp_salary
    def get_department(self):
        '''Get Employee Department'''
        return self.department

    def calculate_emp_salary(self, salary, hours_worked):
        '''To calculate employee salary'''
        self.hours_worked = hours_worked    # No. of hours worked
        if self.hours_worked > 50:
            overtime = hours_worked - 50
            self.overtime_amount = (overtime * (salary / 50))

        return self.overtime_amount

    def emp_assign_department(self, department):
        '''To assign employee department'''
        self.department = department
        return self.department

    def print_employee_details(self):
        '''Print employee details'''
        print(f"{self.emp_name}, {self.emp_id}, {self.emp_salary}, {self.department}")

Employee1 = Employee("E7876", "ADAMS",50000, "ACCOUNTING")
Employee1.get_emp_name()
Employee1.get_emp_id()
Employee1.get_emp_salary()
Employee1.get_department()
Employee1.print_employee_details()
Employee1.emp_assign_department("RESEARCH")
Employee1.print_employee_details()
Employee1.calculate_emp_salary(50000, 51)
print("Overtime Amount:",Employee1.overtime_amount)
Employee2 = Employee( "E7499","JONES", 45000, "RESEARCH")
Employee2.print_employee_details()
