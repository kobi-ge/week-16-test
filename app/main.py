from fastapi import FastAPI

app = FastAPI()

@app.get("/get_engineering_high_salary_employees")
def get_high_salary_engineers():
    pass

@app.get("/get_employees_by_age_and_role")
def get_employees_age_role():
    pass

@app.get("/get_top_seniority_employees_excluding_hr")
def get_top_seniority():
    pass

@app.get("/get_employees_by_age_or_seniority")
def get_emps_by_age_seniority():
    pass

@app.get("/get_managers_excluding_departments")
def get_monagers():
    pass

@app.get("/get_employees_by_lastname_and_age")
def get_emp_name_age():
    pass

