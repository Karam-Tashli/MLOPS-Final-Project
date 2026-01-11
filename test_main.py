from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to MLOps Final Project API"}

def test_create_project_authorized():
    # هنا نرسل المفتاح السري مع الطلب
    response = client.post(
        "/projects/",
        json={"name": "ML Project", "description": "Test Description"},
        headers={"X-API-Key": "mysecretpassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "ML Project"
    assert "id" in data

def test_create_project_unauthorized():
    # هنا نجرب الدخول بدون مفتاح
    response = client.post(
        "/projects/",
        json={"name": "Hacker Project", "description": "Should fail"}
    )
    # التعديل هنا: النظام يعيد 401 عندما يكون المفتاح غير موجود
    assert response.status_code == 401