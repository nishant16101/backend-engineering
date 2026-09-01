#descriptor with set
class PositiveNumber:
    def __get__(self,instance,owner):
        if instance is None:
            return self
        return instance._value
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Number cant be negative")
        instance._value = value

class Product:
    price = PositiveNumber()

p =  Product()
p.price = 100
print(p.price)
