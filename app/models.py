from werkzeug.security import check_password_hash, generate_password_hash
from .config import Config, mongodb_client

client = mongodb_client()
db = client.rbac_db
users_collection = db.users
roles_collection = db.roles

class User:
    @staticmethod
    def create_user(username, password, role="user"):
        hashed_password = generate_password_hash(password)
        user = {'username': username, 'password': hashed_password, 'role': role}
        users_collection.insert_one(user)
    
    @staticmethod
    def find_user_by_username(username):
        return users_collection.find_one({'username': username})
    
    @staticmethod
    def verify_password(stored_password, input_password):
        return check_password_hash(stored_password, input_password)

class Role:
    @staticmethod
    def create_role(role_name, permissions):
        role = {'role_name': role_name, 'permissions': permissions}
        roles_collection.insert_one(role)
    
    @staticmethod
    def get_permissions(role_name):
        role = roles_collection.find_one({'role_name': role_name})
        return role['permissions'] if role else []