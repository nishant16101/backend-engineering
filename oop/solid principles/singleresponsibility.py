# class should have reason to change. Class should do only one thing
#bad example
class UserService:
    def create_user(self,user):
        if not user["email"]:
            raise ValueError("Email required")
        #save to database
        print("INSERT into users")
        #send email
        print("Sending welcome email")

# class has multiple responsibilities
#better design
class UserValidator:
    def validate(self,user):
        if not user["email"]:
            raise ValueError

class UserRepository:
    def save(self,user):
        print("Saving to database")

class EmailService:

    def send_welcome_email(self, email):
        print(f"Sending email to {email}")


class UserService2:
    def __init__(self,validator,repository,email_service):
        self.validator = validator
        self.repository = repository
        self.email_service = email_service

    def create_user(self,user):
        self.validator.validate(user)
        self.repository.save(user)
        self.email_service.send_welcome_email(
            user['email']
        )
        
