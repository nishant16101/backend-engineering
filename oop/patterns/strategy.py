class CardPayment:
    def pay(self,amount):
        print(f"Paid {amount} using card")

class UPIPayment:
    def pay(self,amount):
        print(f"Paid {amount }using upi")

class PayPal:
    def pay(self,amount):
        print(f"Paid {amount} using Paypal")


class PaymentService:
    def __init__(self,strategy):
        self.strategy = strategy

    def checkout(self,amount):
        self.strategy.pay(amount)

service = PaymentService(UPIPayment())
service.checkout(1000)