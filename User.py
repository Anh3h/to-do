"""User's class"""


class User:

    # User class constructor. used to initialize properties of the user's object
    def __init__(self, first_name, last_name):
        self.setFirstName(first_name)
        self.setLastName(last_name)

    # method called print an instance of the User's class as string
    def __str__(self):
        return self._first_name + " " + self._last_name

    # method called to set user's first name
    def setFirstName(self, first_name):
        if len(first_name) > 1:
            self._first_name = first_name
        else:
            raise ValueError("Invalid first name: The first name must be more than one character")

    # method called to get user's first name
    def getFirstName(self):
        return self._first_name

    # method called to set user's last name
    def setLastName(self, last_name):
        if len(last_name) > 1:
            self._last_name = last_name
        else:
            raise ValueError("Invalid last name: The last name must be more than one character")

    # method called to get user's last name
    def getLastName(self):
        return self._last_name