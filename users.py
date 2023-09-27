from mysqlconnection import connectToMySQL
class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    def get_all(cls):
        query="SELECT * FROM users_shema.user;"
        results= connectToMySQL('users_shema').query_db(query)
        users=[]
        for u in results:
            users.append(cls(u))
        return users
    @classmethod
    def creare(cls,data):
        query=" insert into users_shema.user(first_name,last_name,email) values (%(first_name)s,%(last_name)s,%(email)s)"
        result=connectToMySQL('users_shema').query_db(query,data)
        return result
