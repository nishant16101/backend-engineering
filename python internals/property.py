class User:
    def __init__(self,age):
        self._age = age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value <0:
            raise ValueError("Invalid age")
        self._age = value

u = User(25)
print(u.age)
u.age = 30
print(u.age)