#inheritance creates tight coupling between parent and child

class MySQLDatabase:
    def save(self,data):
        print("Saving to mysql")

class UserService:
    def __init__(self, database):
        self.database = database

    def create_user(self, user):
        self.database.save(user)


mysql = MySQLDatabase()
service = UserService(mysql)

service.create_user("Nishant")