from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Student Project Management API", "environment": "Production"}

def test_create_project():
    project_data = {
        "title": "MLOps Automation",
        "student_name": "Test Student",
        "description": "Testing the API",
        "status": "Pending"
    }
    response = client.post("/projects/", json=project_data)
    assert response.status_code == 201
    assert response.json()["title"] == "MLOps Automation"
    assert "id" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}