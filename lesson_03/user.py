class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def seyFirstName(self):
        return print(self.first_name)

    def seyLastName(self):
        return print(self.last_name)

    def FirsLasttName(self):
        return print(f"{self.first_name} {self.last_name}")
