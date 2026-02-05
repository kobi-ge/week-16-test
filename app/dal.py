from rich import print as rprint

from connection import connect_to_mongo
from conversin import convert_objectid_to_str

collection = connect_to_mongo()

def get_engineering_high_salary_employees():
    try:
        query = {"$and":[{"job_role.department": "Engineering"}, {"salary":{"$gt": 65000}}]}
        results = collection.find(query).to_list()
        results_clean = convert_objectid_to_str(results)
        return results_clean
    except Exception as e:
        return f"the following error occured: {e}"
    
def get_employees_by_age_and_role():
    try:
        query = {"$and": [{"age": {"$gte": 30, "$lte": 45}}, {"$or": [{"job_role.title": "Specialist"}, {"job_role.title": "Engineer"}]}]}
        results = collection.find(query).to_list()
        rprint(results)
        results_clean = convert_objectid_to_str(results)
        return results_clean
    except Exception as e:
        return f"the following error occured: {e}"
