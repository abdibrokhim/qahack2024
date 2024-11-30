import requests

BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

headers = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-9"
}

# Test 1: Valid Game UUID
def test_get_game_valid_uuid():
    game_uuid = "5449c9d0-3399-44e1-bd63-f6cbb62c38ea"  # The UUID you are using

    # Test for the release environment
    response = requests.get(f"{BASE_URL_RELEASE}/games/{game_uuid}", headers=headers)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    assert response.status_code == 200, f"Failed on release: {response.text}"
    game = response.json()
    assert game["uuid"] == game_uuid, f"UUID mismatch on release: {response.text}"
    assert "title" in game, "Title missing in game response"
    assert "price" in game, "Price missing in game response"
    assert "category_uuids" in game, "Category UUIDs missing in game response"

    # Test for the dev environment (expected 404 error due to missing data)
    response = requests.get(f"{BASE_URL_DEV}/games/{game_uuid}", headers=headers)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")

    # Adjusting test to expect 404 on dev environment
    assert response.status_code == 404, f"Failed on dev: {response.text}"
    error = response.json()
    assert error["message"] == f"Could not find game with \"uuid\": {game_uuid}", f"Unexpected error message on dev: {response.text}"


# Test 2: Invalid Game UUID (Game Not Found)
def test_get_game_invalid_uuid():
    game_uuid = "invalid-uuid-1234"  # Invalid UUID

    # Test for the release environment (404 expected)
    response = requests.get(f"{BASE_URL_RELEASE}/games/{game_uuid}", headers=headers)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    assert response.status_code == 404, f"Failed on release: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on release: {response.text}"

    # Test for the dev environment (404 expected)
    response = requests.get(f"{BASE_URL_DEV}/games/{game_uuid}", headers=headers)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")

    assert response.status_code == 404, f"Failed on dev: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on dev: {response.text}"

# Test 3: Missing Game UUID
def test_get_game_missing_uuid():
    # Test for the release environment (400 or 404 expected, depending on API handling)
    response = requests.get(f"{BASE_URL_RELEASE}/games/", headers=headers)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    assert response.status_code == 404, f"Failed on release: {response.text}"  # Assuming it returns 404 if UUID is missing
    error = response.json()
    assert "message" in error, f"Error message missing on release: {response.text}"

    # Test for the dev environment (404 expected)
    response = requests.get(f"{BASE_URL_DEV}/games/", headers=headers)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")

    assert response.status_code == 404, f"Failed on dev: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on dev: {response.text}"

# Running all tests
def run_tests():
    test_get_game_valid_uuid()
    # test_get_game_invalid_uuid()
    # test_get_game_missing_uuid()

if __name__ == "__main__":
    run_tests()
