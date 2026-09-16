from fastapi.testclient import TestClient

from src.main import api

client = TestClient(api)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Hello students"} # Updated line

    
def test_create_student():

    response = client.post("/student", json={

        "id": 1,

        "name": "Alice",

        "department": "Computer Science",

        "semester": 5,

        "cgpa": 3.8

    })

    assert response.status_code == 200

    assert response.json()[0]["name"] == "Alice"

def test_get_students():

    response = client.get("/student")

    assert response.status_code == 200

    assert isinstance(response.json(), list)

    assert len(response.json()) > 0

def test_update_student():

    response = client.put("/student/1", json={

        "id": 1,

        "name": "Alice Updated",

        "department": "Computer Science",

        "semester": 6,

        "cgpa": 3.9

    })

    assert response.status_code == 200

    assert response.json()[0]["name"] == "Alice Updated"

def test_update_student_invalid():

    response = client.put("/student/99", json={

        "id": 99,

        "name": "Nobody",

        "department": "None",

        "semester": 1,

        "cgpa": 0.0

    })

    assert response.status_code == 200 

    assert response.json() == {"error": "Student Not Found"}

def test_delete_student():

    response = client.delete("/student/1")

    assert response.status_code == 200

    assert response.json() == {

        "id": 1,

        "name": "Alice Updated",

        "department": "Computer Science",

        "semester": 6,

        "cgpa": 3.9

    }

def test_delete_student_invalid():

    response = client.delete("/student/99")

    assert response.status_code == 200 

    assert response.json() == {"error": "Deletion error"}