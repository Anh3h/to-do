class User:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def __str__(self):
        return self._first_name + " " + self._last_name

    def setFirstName(self, first_name):
        if len(first_name) > 1:
            self._first_name = first_name
        else:
            raise ValueError("Invalid first name: The first name must be more than one character")

    def getFirstName(self):
        return self._first_name

    def setLastName(self, last_name):
        if len(last_name) > 1:
            self._last_name = last_name
        else:
            raise ValueError("Invalid last name: The last name must be more than one character")

    def getLastName(self):
        return self._last_name