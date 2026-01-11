from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import uuid

# --- App Configuration ---
# Title and description help with the auto-generated documentation (Swagger UI)
app = FastAPI(
    title="Student Project Management API",
    description="A RESTful API for managing student graduation projects. Built for MLOps Final Exam.",
    version="1.0.0"
)


# --- Data Models (Pydantic) ---
class ProjectBase(BaseModel):
    title: str
    student_name: str
    description: str
    status: str = "Pending"  # Default status


class Project(ProjectBase):
    id: str


# --- In-Memory Database ---
# Using a list to simulate a database for MVP purposes
projects_db: List[Project] = []


# --- Endpoints ---

@app.get("/", tags=["General"])
def read_root():
    """
    Root endpoint to verify the API is running.
    """
    return {"message": "Welcome to the Student Project Management API", "environment": "Production"}


@app.get("/health", tags=["General"])
def health_check():
    """
    Health check endpoint for Azure/Docker monitoring.
    """
    return {"status": "healthy"}


@app.get("/projects/", response_model=List[Project], tags=["Projects"])
def get_projects():
    """
    Retrieve a list of all registered projects.
    """
    return projects_db


@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED, tags=["Projects"])
def create_project(project: ProjectBase):
    """
    Create a new student project.
    Generates a unique ID automatically.
    """
    new_project = Project(id=str(uuid.uuid4()), **project.model_dump())
    projects_db.append(new_project)
    return new_project


@app.delete("/projects/{project_id}", tags=["Projects"])
def delete_project(project_id: str):
    """
    Delete a project by its unique ID.
    """
    for index, project in enumerate(projects_db):
        if project.id == project_id:
            del projects_db[index]
            return {"message": "Project deleted successfully"}

    raise HTTPException(status_code=404, detail="Project not found")