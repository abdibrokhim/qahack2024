import requests

BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

headers_4 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-4"
}

headers_3 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-3"
}

headers_24 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-24"
}

headers_23 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-23"
}



# Test 1: Create a new user
def test_create_user():
    user_data = {
        "email": "max2@gmail.com",
        "password": "max1@gmail.com",
        "name": "Max1",
        "nickname": "max1"
    }

    # Test for the release environment
    response = requests.post(f"{BASE_URL_RELEASE}/users", headers=headers_3, json=user_data)
    assert response.status_code == 201, f"Failed on release: {response.text}"
    user = response.json()
    assert user["email"] == user_data["email"], f"Email mismatch on release: {response.text}"

    # Test for the dev environment (expected bug)
    response = requests.post(f"{BASE_URL_DEV}/users", headers=headers_3, json=user_data)
    assert response.status_code == 201, f"Failed on dev: {response.text}"
    user = response.json()
    assert user["email"] == user_data["email"], f"Email mismatch on dev (expected bug): {response.text}"

# Test 4: Fetch user details
def test_get_user():
    user_uuid = "515ce5db-c923-4025-82ca-59b604e32355"  # Replace with an actual user UUID
    
    # Test for the release environment
    response = requests.get(f"{BASE_URL_RELEASE}/users/{user_uuid}", headers=headers_23)
    assert response.status_code == 200, f"Failed on release: {response.text}"
    user = response.json()
    assert user["uuid"] == user_uuid, f"UUID mismatch on release: {response.text}"
    print('user:', user)

    # Test for the dev environment (expected bug)
    response = requests.get(f"{BASE_URL_DEV}/users/{user_uuid}", headers=headers_23)
    assert response.status_code == 200, f"Failed on dev: {response.text}"
    user = response.json()
    assert user["uuid"] == user_uuid, f"UUID mismatch on dev (expected bug): {response.text}"
    print('user:', user)

# Test: Update user details
def test_update_user_4():
    user_uuid = "c2c8f767-85b4-47ec-b0e0-e76aefe9e209"  # Replace with actual user UUID

    # New user details for update
    updated_user_data = {
        "email": "max11111@gmail.com",
        "password": "max11111",
        "name": "max11111",
        "nickname": "max11111"
    }

    # Test for the release environment
    response = requests.patch(f"{BASE_URL_RELEASE}/users/{user_uuid}", headers=headers_4, json=updated_user_data)

    # Print detailed response info for debugging
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    if response.status_code == 404:
        print("User not found, please check the user UUID.")
    elif response.status_code == 400:
        print("Bad request, check if the payload is correctly formatted.")
    elif response.status_code == 401:
        print("Unauthorized access, check the authorization token.")
    else:
        print(f"Unexpected status code: {response.status_code}")

    # Proceed with assertions if the request was successful
    assert response.status_code == 200, f"Failed on release: {response.text}"
    user = response.json()
    assert user["email"] == updated_user_data["email"], f"Email mismatch on release: {response.text}"
    assert user["name"] == updated_user_data["name"], f"Name mismatch on release: {response.text}"
    assert user["nickname"] == updated_user_data["nickname"], f"Nickname mismatch on release: {response.text}"
    assert user["uuid"] == user_uuid, f"UUID mismatch on release: {response.text}"


    # Test for the dev environment (expected bug)
    response = requests.patch(f"{BASE_URL_DEV}/users/{user_uuid}", headers=headers_4, json=updated_user_data)
    assert response.status_code == 200, f"Failed on dev: {response.text}"
    
    # Fetch updated user data
    user = response.json()
    assert user["email"] == updated_user_data["email"], f"Email mismatch on dev (expected bug): {response.text}"
    assert user["name"] == updated_user_data["name"], f"Name mismatch on dev (expected bug): {response.text}"
    assert user["nickname"] == updated_user_data["nickname"], f"Nickname mismatch on dev (expected bug): {response.text}"
    assert user["uuid"] == user_uuid, f"UUID mismatch on dev (expected bug): {response.text}"

# Test: Update user details
def test_update_user_24():
    # user_uuid = "515ce5db-c923-4025-82ca-59b604e32355"  # Replace with actual user UUID
    user_uuid = "c2c8f767-85b4-47ec-b0e0-e76aefe9e209"  # Replace with actual user UUID

    # New user details for update
    updated_user_data = {
        "email": "max11111@gmail.com",
        "password": "max11111",
        "name": "max11111",
        "nickname": "max11111"
    }

    # Test for the release environment
    response = requests.patch(f"{BASE_URL_RELEASE}/users/{user_uuid}", headers=headers_24, json=updated_user_data)

    # Print detailed response info for debugging
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    if response.status_code == 404:
        print("User not found, please check the user UUID.")
    elif response.status_code == 400:
        print("Bad request, check if the payload is correctly formatted.")
    elif response.status_code == 401:
        print("Unauthorized access, check the authorization token.")
    else:
        print(f"Unexpected status code: {response.status_code}")

    # Proceed with assertions if the request was successful
    assert response.status_code == 200, f"Failed on release: {response.text}"
    user = response.json()
    assert user["email"] == updated_user_data["email"], f"Email mismatch on release: {response.text}"
    assert user["name"] == updated_user_data["name"], f"Name mismatch on release: {response.text}"
    assert user["nickname"] == updated_user_data["nickname"], f"Nickname mismatch on release: {response.text}"
    assert user["uuid"] == user_uuid, f"UUID mismatch on release: {response.text}"
    print('release done, no bug')


    # Test for the dev environment (expected bug)
    response = requests.patch(f"{BASE_URL_DEV}/users/{user_uuid}", headers=headers_24, json=updated_user_data)
    assert response.status_code == 200, f"Failed on dev: {response.text}"
    
    # Fetch updated user data
    user = response.json()
    assert user["email"] == updated_user_data["email"], f"Email mismatch on dev (expected bug): {response.text}"
    assert user["name"] == updated_user_data["name"], f"Name mismatch on dev (expected bug): {response.text}"
    assert user["nickname"] == updated_user_data["nickname"], f"Nickname mismatch on dev (expected bug): {response.text}"
    assert user["uuid"] == user_uuid, f"UUID mismatch on dev (expected bug): {response.text}"
    print('dev done, no bug')

# Running all tests
def run_tests():
    # test_create_user()
    # test_create_payment()
    # test_get_user()
    test_update_user_4()
    # test_update_user_24()

if __name__ == "__main__":
    run_tests()
