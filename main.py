from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# --- Security Setup (Identity Management) ---
API_KEY = "mysecretpassword"  # هذا هو المفتاح السري
api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials (Wrong API Key)"
        )
    return api_key
# ---------------------------------------------

# Models
class ProjectBase(BaseModel):
    name: str
    description: str
    status: str = "Active"

class Project(ProjectBase):
    id: str

# In-memory database
projects_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to MLOps Final Project API"}

# Public Endpoint (Anyone can see projects)
@app.get("/projects/", response_model=List[Project])
def get_projects():
    return projects_db

# Protected Endpoint (Only authorized users can create projects)
# لاحظ إضافة depends هنا لحماية الرابط
@app.post("/projects/", response_model=Project, dependencies=[Depends(verify_api_key)])
def create_project(project: ProjectBase):
    new_project = Project(id=str(uuid.uuid4()), **project.model_dump())
    projects_db.append(new_project)
    return new_project