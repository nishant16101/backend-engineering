# Software entities should be open for extension but closed for modification
#bad example
class DiscountService:

    def calculate(self, customer_type, price):

        if customer_type == "regular":
            return price

        elif customer_type == "premium":
            return price * 0.9

        elif customer_type == "employee":
            return price * 0.8

# better design
class RegularDiscount:
    def calculate(self,price):
        return price
class PremiumDiscount:
    def calculate(self,price):
        return price * 0.9

class EmployeeDiscount:
    def calculate(self,price):
        return price * 0.8

class DiscountService2:
    def __init__(self,strategy):
        self.strategy = strategy

    def calculate(self,price):
        return self.strategy.calculate(price)

service = DiscountService2(PremiumDiscount())

print(service.calculate(1000))
    