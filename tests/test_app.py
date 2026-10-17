from app.main import app


def test_homepage_returns_dashboard():
    app.testing = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"DevOps Cloud Status Dashboard" in response.data
    assert b"System Overview" in response.data
    assert b"GitHub Actions" in response.data
    assert b"Microsoft Azure" in response.data


def test_health_endpoint_returns_healthy():
    app.testing = True

    with app.test_client() as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
