import requests

BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

headers = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-24"
}

# Test: Update user details
def test_update_user():
    user_uuid = "3cfe26ab-5455-49fa-a173-020adaa2d52d"  # Replace with actual user UUID

    # New user details for update
    updated_user_data = {
        "email": "max12@gmail.com",
        "password": "password12",
        "name": "Max12",
        "nickname": "max11aa1"
    }

    # Test for the release environment
    response = requests.patch(f"{BASE_URL_RELEASE}/users/{user_uuid}", headers=headers, json=updated_user_data)
    # print('response:', response.json())
    assert response.status_code == 200, f"Failed on release: {response.text}"
    
    # Fetch updated user data
    user = response.json()
    assert user["email"] == updated_user_data["email"], f"Email mismatch on release: {response.text}"
    assert user["name"] == updated_user_data["name"], f"Name mismatch on release: {response.text}"
    assert user["nickname"] == updated_user_data["nickname"], f"Nickname mismatch on release: {response.text}"

    # Test for the dev environment (expected bug)
    response = requests.patch(f"{BASE_URL_DEV}/users/{user_uuid}", headers=headers, json=updated_user_data)
    assert response.status_code == 200, f"Failed on dev: {response.text}"
    
    # Fetch updated user data
    user = response.json()
    assert user["email"] == updated_user_data["email"], f"Email mismatch on dev (expected bug): {response.text}"
    assert user["name"] == updated_user_data["name"], f"Name mismatch on dev (expected bug): {response.text}"
    assert user["nickname"] == updated_user_data["nickname"], f"Nickname mismatch on dev (expected bug): {response.text}"

# Running the test
def run_tests():
    test_update_user()

if __name__ == "__main__":
    run_tests()
