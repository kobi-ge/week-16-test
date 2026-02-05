from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json

load_dotenv()


host = os.getenv("MONGO_HOST")
port= int(os.getenv("MONGO_PORT"))
username= os.getenv("MONGO_USERNAME")
password=os.getenv("MONGO_PASSWORD")
uri = f"mongodb://{username}:{password}@{host}:{port}"
print(uri)


def load_db(Collection):
    with open('employee_data_advanced.json') as file:
        file_data = json.load(file)

    # Inserting the loaded data in the Collection
    ins_result = Collection.insert_many(file_data)
    print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")

def connect_to_mongo():
    try:
        client = MongoClient(uri)
        client.admin.command("ping")
        print("connection established")
        db = client['mydb']
        collection = db['mycoll']
        print(collection)
        load_db(collection)
        return collection
    except Exception as e:
        print(f"connection failed: {e}")
        return None

