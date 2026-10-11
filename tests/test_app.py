from app.main import app


def test_homepage_returns_project_status():
    app.testing = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["project"] == "DevOps Cloud Status Dashboard"
    assert data["status"] == "running"
    assert data["message"] == "Application is working!"


def test_health_endpoint_returns_healthy():
    app.testing = True

    with app.test_client() as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
