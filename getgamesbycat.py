import requests

BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

headers = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-10"
}

# Test 1: Valid Category UUID
def test_get_games_by_category_valid_uuid():
    category_uuid = "e86aecef-fe7a-4164-a324-57503df14ab9"  # Replace with actual category UUID

    # Test for the release environment
    response = requests.get(f"{BASE_URL_RELEASE}/categories/{category_uuid}/games", headers=headers)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    assert response.status_code == 200, f"Failed on release: {response.text}"
    data = response.json()
    assert "games" in data, "Games field missing in response"
    assert "meta" in data, "Meta field missing in response"
    assert isinstance(data["games"], list), "Games should be a list"
    assert len(data["games"]) > 0, "No games returned"

    # Test for the dev environment (expected bug or missing data)
    response = requests.get(f"{BASE_URL_DEV}/categories/{category_uuid}/games", headers=headers)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")

    assert response.status_code == 200, f"Failed on dev: {response.text}"
    data = response.json()
    assert "games" in data, "Games field missing in response"
    assert "meta" in data, "Meta field missing in response"
    assert isinstance(data["games"], list), "Games should be a list"
    assert len(data["games"]) > 0, "No games returned"

# Test 2: Invalid Category UUID (Category Not Found)
def test_get_games_by_category_invalid_uuid():
    category_uuid = "invalid-category-uuid"  # Invalid category UUID

    # Test for the release environment (404 expected)
    response = requests.get(f"{BASE_URL_RELEASE}/categories/{category_uuid}/games", headers=headers)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    assert response.status_code == 404, f"Failed on release: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on release: {response.text}"

    # Test for the dev environment (404 expected)
    response = requests.get(f"{BASE_URL_DEV}/categories/{category_uuid}/games", headers=headers)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")

    assert response.status_code == 404, f"Failed on dev: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on dev: {response.text}"

# Test 3: Missing Category UUID (Expected 404)
def test_get_games_by_category_missing_uuid():
    # Test for the release environment (404 expected due to missing UUID)
    response = requests.get(f"{BASE_URL_RELEASE}/categories//games", headers=headers)
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    assert response.status_code == 404, f"Failed on release: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on release: {response.text}"

    # Test for the dev environment (404 expected due to missing UUID)
    response = requests.get(f"{BASE_URL_DEV}/categories//games", headers=headers)
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")

    assert response.status_code == 404, f"Failed on dev: {response.text}"
    error = response.json()
    assert "message" in error, f"Error message missing on dev: {response.text}"

# Test 4: Pagination (Offset and Limit)
def test_get_games_by_category_with_pagination():
    category_uuid = "e86aecef-fe7a-4164-a324-57503df14ab9"  # Replace with actual category UUID
    limit = 5
    offset = 0

    # Test for the release environment with pagination
    response = requests.get(f"{BASE_URL_RELEASE}/categories/{category_uuid}/games", headers=headers, params={"limit": limit, "offset": offset})
    print(f"Release Environment Response Status Code: {response.status_code}")
    print(f"Release Environment Response Text: {response.text}")

    assert response.status_code == 200, f"Failed on release: {response.text}"
    data = response.json()
    assert "games" in data, "Games field missing in response"
    assert "meta" in data, "Meta field missing in response"
    assert isinstance(data["games"], list), "Games should be a list"
    assert len(data["games"]) == limit, f"Expected {limit} games, got {len(data['games'])}"

    # Test for the dev environment with pagination (expected bug or discrepancy)
    response = requests.get(f"{BASE_URL_DEV}/categories/{category_uuid}/games", headers=headers, params={"limit": limit, "offset": offset})
    print(f"Dev Environment Response Status Code: {response.status_code}")
    print(f"Dev Environment Response Text: {response.text}")

    assert response.status_code == 200, f"Failed on dev: {response.text}"
    data = response.json()
    assert "games" in data, "Games field missing in response"
    assert "meta" in data, "Meta field missing in response"
    assert isinstance(data["games"], list), "Games should be a list"
    assert len(data["games"]) == limit, f"Expected {limit} games, got {len(data['games'])}"

# Running all tests
def run_tests():
    test_get_games_by_category_valid_uuid()
    # test_get_games_by_category_invalid_uuid()
    test_get_games_by_category_missing_uuid()
    test_get_games_by_category_with_pagination()

if __name__ == "__main__":
    run_tests()
