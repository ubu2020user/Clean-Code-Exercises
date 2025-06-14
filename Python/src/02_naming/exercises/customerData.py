from datetime import date
from dateutil.relativedelta import relativedelta  # pip3 install python-dateutil

class employee_data:
    maxHours = 40

    def __init__(self, fname, lname, addr_st, addr_zip, addr_cty, wage, hrsWorked, hireDate):
        self.fname = fname
        self.lname = lname
        self.addr_st = addr_st
        self.addr_zip = addr_zip
        self.addr_cty = addr_cty
        self.wage = wage
        self.hrsWorked = hrsWorked
        self.hireDate = hireDate

    def calcWeeklySal(self):
        return self.wage * self.hrsWorked

    def calcYearsService(self):
        today = date.today()
        return relativedelta(today, self.hireDate).years

# Example usage of the class
emp = employee_data("John", "Doe", "Office Street 1", "54321", "Office City", 20, 35, date(2015, 3, 15))
print("Weekly Salary:", emp.calcWeeklySal())
print("Years of Service:", emp.calcYearsService())
