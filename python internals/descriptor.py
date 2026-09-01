# A descriptor is an object that defines one or more of this methods - [__get__(),__set__(),__delete__()]
# An object becomes descriptor when it implements these methods

class MyDescriptor:
    def __get__(self,instance,owner):
        print("GET Called")
        return 100
class User:
    age = MyDescriptor()
u = User()
print(u.age)
print(User.__dict__["age"])
print(u.__dict__)


#python effictively invokes - MyDescriptor.__get__(descriptor, u, User)