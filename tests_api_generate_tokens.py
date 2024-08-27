from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_generate_tokens():
    # Test case 1: Valid API key and text
    response = client.post(
        "/api/generate-tokens",
        json={"text": "Hello, World!"},
        headers={"access_token": "malhar"}
    )
    assert response.status_code == 200
    assert "checksum" in response.json()

    # Test case 2: Invalid API key
    response = client.post(
        "/api/generate-tokens",
        json={"text": "Hello, World!"},
        headers={"access_token": "invalid_key"}
    )
    assert response.status_code == 401
    assert "Unauthorized" in response.text

    # Test case 3: Missing API key
    response = client.post(
        "/api/generate-tokens",
        json={"text": "Hello, World!"}
    )
    assert response.status_code == 401
    assert "Unauthorized" in response.text

    # Test case 4: Missing text
    response = client.post(
        "/api/generate-tokens",
        json={}
    )
    assert response.status_code == 422
    assert "field required" in response.text

    # Add more test cases as needed

if __name__ == "__main__":
    test_api_generate_tokens()client = TestClient(app)

def test_api_generate_tokens():
    # Test case 1: Valid API key and text
    response = client.post(
        "/api/generate-tokens",
        json={"text": "Hello, World!"},
        headers={"access_token": "malhar"}
    )
    assert response.status_code == 200