from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


host = os.getenv("MONGO_HOST")
port= int(os.getenv("MONGO_PORT"))
username= os.getenv("MONGO_USERNAME")
password=os.getenv("MONGO_PASSWORD")
uri = f"mongodb://{username}:{password}@{host}:{port}"

