class EmailNotification:
    def send(self,message):
        print("Sending email",message)

class SMSNotification:
    def send(self,message):
        print("Sending sms",message)

class PushNotification:
    def send(self,messaage):
        print("Sending Push",messaage)


class NotificationFactory:
    @staticmethod
    def create(notification_type):
        if notification_type == "email":
            return EmailNotification()
        if notification_type == "sms":
            return SMSNotification()
        if notification_type == "push":
            return PushNotification()
        raise ValueError("Unknown notification type")



notification = NotificationFactory.create("email")
notification.send("Order Shipped")