#singleton means ensure that class has only one instance with given scope process and provide access to it
class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1  = DatabaseConnection()
db2 = DatabaseConnection()


print(db1 is db2)