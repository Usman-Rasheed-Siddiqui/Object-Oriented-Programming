
class Employee:
    def __init__(self):
        self.employee_id =input("Enter Employee ID: ")
        self.employee_name = input("Enter Employee name: ")
        self.designation = input("Enter designation: ")

    def ShowInfo(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Designation: {self.designation}")

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.manager_performance = input("Enter manager's performance: ")
        self.no_of_teams_managed = int(input("Enter number of teams being managed: "))

    def ShowInfo(self):
        super().ShowInfo()
        print(f"Manager Performance: {self.manager_performance}")
        print(f"No of Teams Being Managed: {self.no_of_teams_managed}")

class Clerk(Employee):
    def __init__(self,timing, name=''):
        super().__init__()
        self.teamName = name
        self.timings = timing

    def ShowInfo(self):
        super().ShowInfo()
        print(f"Team Name: {self.teamName}")
        print(f"Timings: {self.timings} hrs")

c1 = Clerk(4, "Dolphins")
c1.ShowInfo()
c2 = Manager()
c2.ShowInfo()