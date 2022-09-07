class Animal:
    def __init__(self, name_, age_):
        self.name = name_
        self.age = age_

    def getAge(self):
        return self.age

    def setAge(self, age_):
        if age_ < 0:
            return False
        if self.age != age_:
            self.age = age_
            return True
