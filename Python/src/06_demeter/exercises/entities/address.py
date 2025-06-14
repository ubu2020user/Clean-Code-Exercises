class Address:
    """
    Represents an employee's address information.
    
    Attributes:
        street (str): The street name including house number
        city (str): The city name
        postal_code (str): Postal code
        country (str): Country name
    """
    
    def __init__(self, street, city, postal_code, country="USA"):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.country = country
        
    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}, {self.country}"
        
    def is_domestic(self):
        """Check if address is within the default country."""
        return self.country == "USA"