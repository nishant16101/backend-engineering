class EmailSender:
    def send(self,message):
        print(f"Email:{message}")

class SMSSender:
    def send(self,message):
        print(f"Message:{message}")

def notify(sender):
    sender.send("Order Shipped")

notify(EmailSender())
notify(SMSSender())