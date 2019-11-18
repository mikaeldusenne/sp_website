from pymongo import MongoClient
import yaml
import logging
logger = logging.getLogger(__name__)

from src.types import User

with open("./auth.yaml") as f:
    admin_password = yaml.load(f, Loader=yaml.SafeLoader)["db"]["admin"]

client = MongoClient('mongo_docker',
            username='admin',
            password=admin_password,
            authSource='thedb')


db = client.thedb


def get_users():
    try:
        return list(db.users.find())
    except Exception as e:
        return None

def get_user(user):
    print("db: get user", user)
    try:
        u = db.users.find_one({"id": user})
        print(u)
        return u
    except Exception as e:
        print(e)
        return None

def add_user(user):
    assert type(user) == User
    try:
        db.users.insert_one(user.__dict__)
        return True
    except Exception as e:
        print(e)
        

# db.users.create_index([("id", pymongo.ASCENDING),
#                        ("email", pymongo.ASCENDING)],
#                       unique=True)






