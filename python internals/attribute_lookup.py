class User:
    role = "user"
    def __init__(self,name):
        self.name = name
u = User("Nishant")

print(User.__dict__)
print(u.__dict__)
print(u.role)

"""obj.attribute
      ↓
__getattribute__()
      ↓
descriptor lookup
      ↓
instance dictionary
      ↓
class / MRO
      ↓
__getattr__() if defined
      ↓
AttributeError """