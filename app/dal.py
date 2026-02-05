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

def get_top_seniority_employees_excluding_hr():
    try:
        query = {"job_role.department": {"$ne": "HR"}}
        results = collection.find(query).sort({"years_at_company": -1}).limit(7).to_list()
        rprint(results)
        results_clean = convert_objectid_to_str(results)
        return results_clean
    except Exception as e:
        return f"the following error occured: {e}"
    
def get_employees_by_age_or_seniority():
    try:
        query = {"$or": [{"age": {"$gt": 50}}, {"years_at_company": {"$lt": 3}}]}
        select = {"_id": 0, "employee_id": 1, "name": 1, "age": 1, "years_at_company": 1}
        results = collection.find(query, select).to_list()
        rprint(results)
        return results
    except Exception as e:
        return f"the following error occured: {e}"
    
def get_managers_excluding_departments():
    try:
        query = {"$and": [{"job_role.title": "Manager"}, {"$and": [{"job_role.department": {"$ne": "Sales"}}, {"job_role.department": {"$ne": "Marketing"}}]}]}
        results = collection.find(query).to_list()
        results_clean = convert_objectid_to_str(results)
        return results_clean
    except Exception as e:
        return f"the following error occured: {e}"
    
def get_employees_by_lastname_and_age():
    try:
        query = {"$and": [{"$or": [{"name": {"$regex": "Wright$"}}, {"name": {"$regex": "Nelson$"}}]}, {"age": {"$lt": 35}}]}
        select = {"name": 1, "age": 1, "job_role.department": 1, "_id": 0}
        results = collection.find(query, select).to_list()
        return results
    except Exception as e:
        return f"the following error occured: {e}"
