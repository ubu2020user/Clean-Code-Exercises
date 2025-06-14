from datetime import date
from dateutil.relativedelta import relativedelta  

class EmployeeData:
    """
    A class to represent employee data and perform calculations related to their salary and years of service.
    Attributes:
        MAX_HOURS (int): The maximum number of hours an employee can work in a week.
        first_name (str): The first name of the employee.
        last_name (str): The last name of the employee.
        street_address (str): The street address of the employee.
        zip_code (str): The zip code of the employee's address.
        city (str): The city of the employee's address.
        hourly_wage (float): The hourly wage of the employee.
        hours_worked (int): The number of hours worked by the employee in a week.
        hire_date (datetime.date): The date the employee was hired.
    Methods:
        calculate_weekly_salary():
            Calculates the weekly salary of the employee based on their hourly wage and hours worked.
        calculate_years_of_service():
            Calculates the number of years the employee has been in service based on their hire date.
    """
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
