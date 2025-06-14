from datetime import date
from dateutil.relativedelta import relativedelta  # pip3 install python-dateutil

class EmployeeData:
    MAX_HOURS = 40

    def __init__(self, first_name, last_name, street_address, zip_code, city, hourly_wage, hours_worked, hire_date):
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.zip_code = zip_code
        self.city = city
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.hire_date = hire_date

    def calculate_weekly_salary(self):
        return self.hourly_wage * self.hours_worked

    def calculate_years_of_service(self):
        today = date.today()
        return relativedelta(today, self.hire_date).years


# Example usage of the class
employee = EmployeeData(
    first_name="John",
    last_name="Doe",
    street_address="Office Street 1",
    zip_code="54321",
    city="Office City",
    hourly_wage=20,
    hours_worked=35,
    hire_date=date(2015, 3, 15)
)

print("Weekly Salary:", employee.calculate_weekly_salary())
print("Years of Service:", employee.calculate_years_of_service())
