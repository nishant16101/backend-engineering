#abstract classes are designed to provide a blueprint for other classes. They cant be instantiated directly.Typically used to define properties that subclass must implement

from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class StripePayment(PaymentGateway):
    def pay(self,amount):
        print(f"Stripe payment:{amount}")

class Razorpay(PaymentGateway):
    def pay(self,amount):
        print(f"Razorpay payment{amount}")

razorpay = Razorpay()
stripe = StripePayment()
razorpay.pay(1000)
stripe.pay(1000)