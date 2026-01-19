import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test for root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert str(response.url).endswith("/static/index.html")

# Test for getting activities
def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert "Chess Club" in activities

# Test for signing up for an activity
def test_signup_for_activity():
    response = client.post("/activities/Chess%20Club/signup?email=testuser@mergington.edu")
    assert response.status_code == 200
    assert response.json() == {"message": "Signed up testuser@mergington.edu for Chess Club"}

# Test for unregistering from an activity
def test_unregister_from_activity():
    response = client.delete("/activities/Chess%20Club/unregister?email=testuser@mergington.edu")
    assert response.status_code == 200
    assert response.json() == {"message": "Unregistered testuser@mergington.edu from Chess Club"}