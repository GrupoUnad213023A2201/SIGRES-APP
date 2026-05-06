import re

class Customer:
    def __init__(self, id_number, name, email):
        # Assigning values through setters to trigger validation
        self.id_number = id_number
        self.name = name
        self.email = email

    # --- Encapsulation and Validation for 'id_number' ---
    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, value):
        if not str(value).isdigit():
            raise ValueError("ID number must contain only digits.")
        self.__id_number = str(value)

    # --- Encapsulation and Validation for 'name' ---
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not str(value).strip():
            raise ValueError("Customer name cannot be empty.")
        self.__name = str(value).strip()

    # --- Encapsulation and Validation for 'email' ---
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, str(value)):
            raise ValueError("Invalid email address format.")
        self.__email = str(value)

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.id_number} | Email: {self.email})"