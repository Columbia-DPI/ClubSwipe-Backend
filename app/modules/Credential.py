from dotenv import load_dotenv
load_dotenv()
import os

MONGO_UNAME = os.getenv("MONGO_UNAME")
MONGO_PASS = os.getenv("MONGO_PASS")

def getMongoID():
    return MONGO_UNAME

def getMongoPass():
    return MONGO_PASS