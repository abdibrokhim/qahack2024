import requests

BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

headers = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-7"
}

# Test 1: Valid Login
def test_valid_login():
    login_data = {
        "email": "max11112@gmail.com",
        "password": "password12"
    }

    # Test for the release environment
    response = requests.post(f"{BASE_URL_RELEASE}/users/login", headers=headers, json=login_data)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")
    
    assert response.status_code == 200, f"Failed on release: {response.text}"
    user = response.json()
    assert "uuid" in user, "User UUID not returned on release"
    assert user["email"] == login_data["email"], f"Email mismatch on release: {response.text}"

    # Test for the dev environment (expected bug)
    response = requests.post(f"{BASE_URL_DEV}/users/login", headers=headers, json=login_data)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")
    
    assert response.status_code == 200, f"Failed on dev: {response.text}"
    user = response.json()
    assert "uuid" in user, "User UUID not returned on dev"
    assert user["email"] == login_data["email"], f"Email mismatch on dev: {response.text}"

# Test 2: Invalid Login (Wrong Credentials)
def test_invalid_login():
    login_data = {
        "email": "max11@gmail.com",
        "password": "wrongpassword"
    }

    # Test for the release environment (404 expected)
    response = requests.post(f"{BASE_URL_RELEASE}/users/login", headers=headers, json=login_data)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")
    
    assert response.status_code == 404, f"Failed on release: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on release: {response.text}"

    # Test for the dev environment (404 expected)
    response = requests.post(f"{BASE_URL_DEV}/users/login", headers=headers, json=login_data)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")
    
    assert response.status_code == 404, f"Failed on dev: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on dev: {response.text}"

# Test 3: Missing Credentials (Expected 400 Bad Request)
def test_missing_credentials():
    login_data = {
        "email": "max11@gmail.com"
        # Missing password
    }

    # Test for the release environment (400 expected)
    response = requests.post(f"{BASE_URL_RELEASE}/users/login", headers=headers, json=login_data)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")
    
    assert response.status_code == 400, f"Failed on release: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on release: {response.text}"

    # Test for the dev environment (400 expected)
    response = requests.post(f"{BASE_URL_DEV}/users/login", headers=headers, json=login_data)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")
    
    assert response.status_code == 400, f"Failed on dev: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on dev: {response.text}"

# Running all tests
def run_tests():
    test_valid_login()
    # test_invalid_login()
    # test_missing_credentials()

if __name__ == "__main__":
    run_tests()