#This pattern separates the business logic from database access

#define repository
class UserRepository:
    def find_by_id(self,user_id):
        raise NotImplementedError

#Implementation
class PostgresUserRepo(UserRepository):
    def find_by_id(self,user_id):
        #postgress query
        return {
            id:user_id,
            "name":"Nishant"
        }


#service
class UserService:
    def __init__(self,repository):
        self.repository = repository

    def get_user(self,user_id):
        self.repository.find_by_id(user_id)

repository = PostgresUserRepo()
service = UserService(repository)

user = service.get_user(10)
print(user)