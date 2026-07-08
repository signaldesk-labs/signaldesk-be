from app.main import create_app

def test_dashboard_contract():
    client = create_app().test_client()
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    payload = response.get_json()
    assert {"metrics", "events", "trend"} <= payload.keys()

def test_rest_auth_refresh():
    client = create_app().test_client()
    response = client.post("/api/auth/refresh")
    assert response.status_code == 200
    assert "accessToken" in response.get_json()
