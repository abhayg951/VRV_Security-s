from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    MONGO_URI = os.getenv('MONGO_URI', "mongodb://localhost:27017/rbac_db")

def mongodb_client():
    return MongoClient(Config.MONGO_URI)