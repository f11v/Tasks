from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_task():
    response = client.post("/tasks", json={
        "id": 1,
        "name": "Tarea 1",
        "title": "Comprar comida",
        "completed": False
    })
    assert response.status_code == 200

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "Tarea 1",
        "title": "Comprar comida",
        "completed": False
    }]