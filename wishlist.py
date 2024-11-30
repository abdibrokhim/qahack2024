import requests
import json

# Set up for both environments
BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

HEADERS = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-6"
}

HEADERS_API_25 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-25"
}

HEADERS_API_5 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-5"
}

HEADERS_API_8 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-8"
}

# Test Case 1: Get Wishlist
def test_get_wishlist(user_uuid):
    print("\n---Testing Get Wishlist---")
    for base_url in [BASE_URL_RELEASE, BASE_URL_DEV]:
        print(f"Testing Get Wishlist in environment: {base_url}")
        response = requests.get(f"{base_url}/users/{user_uuid}/wishlist", headers=HEADERS)
        assert response.status_code == 200, f"Failed to get wishlist in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data, "No items in wishlist"
        print(f"Wishlist for {user_uuid} in {base_url}: {data}")

# Test Case 2: Add Item to Wishlist
def test_add_to_wishlist_25(user_uuid, game_uuid):
    print("\n---Testing Add Item to Wishlist---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_25), (BASE_URL_DEV, HEADERS_API_25)]:
        print(f"Testing Add Item to Wishlist in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/wishlist/add", headers=headers, json={"item_uuid": game_uuid})
        assert response.status_code == 200, f"Failed to add item in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data, "Failed to add item"
        print(f"Updated Wishlist in {base_url}: {data}")

# Test Case 2: Add Item to Wishlist
def test_add_to_wishlist_5(user_uuid, game_uuid):
    print("\n---Testing Add Item to Wishlist---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_5), (BASE_URL_DEV, HEADERS_API_5)]:
        print(f"Testing Add Item to Wishlist in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/wishlist/add", headers=headers, json={"item_uuid": game_uuid})
        assert response.status_code == 200, f"Failed to add item in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data, "Failed to add item"
        print(f"Updated Wishlist in {base_url}: {data}")

# Test Case 3: Remove Item from Wishlist
def test_remove_from_wishlist(user_uuid, game_uuid):
    print("\n---Testing Remove Item from Wishlist---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_8), (BASE_URL_DEV, HEADERS_API_8)]:
        print(f"Testing Remove Item from Wishlist in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/wishlist/remove", headers=headers, json={"item_uuid": game_uuid})
        assert response.status_code == 200, f"Failed to remove item in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data, "Failed to remove item"
        print(f"Updated Wishlist in {base_url}: {data}")

# Example Test Execution
user_uuid = "515ce5db-c923-4025-82ca-59b604e32355"  # Valid user UUID
game_uuid = "77a94eec-38e0-4a08-a3d7-2be1007ef686"  # Example valid game UUID
games = ["1990ecdd-4d3d-4de2-91b9-d45d794c82bc", "0378c074-92d6-4d8c-b6d3-878c08dbe27f", "03dbad48-ad81-433d-9901-dd5332f5d9ee", "cb620f56-daa4-43e0-b4a0-e80f8e5be279", "aca79a7c-5b66-4ff2-b3b8-57e56fc053a7", "09531e2b-c3eb-4338-a002-cc4817a7cc58", "77a94eec-38e0-4a08-a3d7-2be1007ef686", "12dc6bb3-cd3f-412a-86fe-3c1dce867481", "06520f6e-5096-4d49-a044-136357737eff", "5449c9d0-3399-44e1-bd63-f6cbb62c38ea"]
rest_games = ["77a94eec-38e0-4a08-a3d7-2be1007ef686", "12dc6bb3-cd3f-412a-86fe-3c1dce867481", "06520f6e-5096-4d49-a044-136357737eff", "5449c9d0-3399-44e1-bd63-f6cbb62c38ea"]
invalid_user_uuid = "invalid-user-uuid"  # Invalid user UUID
invalid_game_uuid = "invalid-game-uuid"  # Invalid game UUID

# Run the tests
# test_get_wishlist(user_uuid)  # Valid user UUID

# for game in rest_games:
    # test_add_to_wishlist_5(user_uuid, game)  # Valid user UUID and game UUID
    # test_remove_from_wishlist(user_uuid, game)  # Valid user UUID and game UUID
# test_add_to_wishlist_25(user_uuid, game_uuid)  # Valid user UUID and game UUID
# test_add_to_wishlist_5(user_uuid, game_uuid)  # Valid user UUID and game UUID
test_remove_from_wishlist(user_uuid, game_uuid)  # Valid user UUID and game UUID
# test_get_wishlist(user_uuid)  # Valid user UUID
# test_get_wishlist(user_uuid)  # Valid user UUID

# Invalid tests to simulate failures (for Dev environment)
# print("\n---Simulating Invalid Tests---")
# test_get_wishlist(invalid_user_uuid)  # Invalid user UUID
# test_add_to_wishlist(invalid_user_uuid, game_uuid)  # Invalid user UUID and valid game UUID
# test_remove_from_wishlist(invalid_user_uuid, invalid_game_uuid)  # Invalid user UUID and invalid game UUID
