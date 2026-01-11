# MLOps Final Project - API & CI/CD Pipeline 🚀

This project demonstrates a complete MLOps workflow using **FastAPI**, **Docker**, and **GitHub Actions**. It provides a secured REST API for managing machine learning projects with automated testing and continuous integration.

## 🌟 Key Features
* **Web API:** Built with FastAPI (High performance).
* **Identity Management:** Secured endpoints using API Key authentication.
* **Containerization:** Fully dockerized application.
* **CI/CD Automation:** GitHub Actions pipeline for automated testing and building.
* **Testing:** 100% test coverage using Pytest.

## 🛠️ How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Karam-Tashli/MLOPS-Final-Project.git](https://github.com/Karam-Tashli/MLOPS-Final-Project.git)
    cd MLOPS-Final-Project
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Server:**
    ```bash
    uvicorn main:app --reload
    ```
    *The API will be available at: `http://127.0.0.1:8000`*

## 🧪 How to Run Tests
To execute the automated unit tests, run:
```bash
pytest

---
## Team Members
* **Student 1:** Karam Tashli
* **ID Student 1:** 165825
* **Student 2:** [Ibrahim Alsayed]
* **ID Student 2:** 160247