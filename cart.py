import requests

# Set up for both environments
BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

# Headers with correct X-Task-Id for each API
HEADERS_API_12 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-12"
}

HEADERS_API_13 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-13"
}

HEADERS_API_14 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-14"
}

HEADERS_API_15 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-15"
}

# Test Case 1: Get Cart
def test_get_cart(user_uuid):
    print("\n---Testing Get Cart---")
    for base_url in [BASE_URL_RELEASE, BASE_URL_DEV]:
        print(f"Testing Get Cart in environment: {base_url}")
        response = requests.get(f"{base_url}/users/{user_uuid}/cart", headers=HEADERS_API_12)
        assert response.status_code == 200, f"Failed to get cart in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data, "No items in cart"
        print(f"Cart for {user_uuid} in {base_url}: {data}")
        length = len(data["items"])
        print(f"Length of Cart for {user_uuid} in {base_url}: {length}")

# Test Case 2: Add Item to Cart
def test_add_to_cart(user_uuid, game_uuid, quantity):
    print("\n---Testing Add Item to Cart---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_13), (BASE_URL_DEV, HEADERS_API_13)]:
        print(f"Testing Add Item to Cart in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/cart/add", headers=headers, json={"item_uuid": game_uuid, "quantity": quantity})
        assert response.status_code == 200, f"Failed to add item in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data, "Failed to add item"
        print(f"Updated Cart in {base_url}: {data}")

# Test Case 3: Change Item Quantity in Cart
def test_change_in_cart(user_uuid, game_uuid, quantity):
    print("\n---Testing Change Item Quantity in Cart---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_13), (BASE_URL_DEV, HEADERS_API_13)]:
        print(f"Testing Change Item Quantity in Cart in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/cart/change", headers=headers, json={"item_uuid": game_uuid, "quantity": quantity})
        assert response.status_code == 200, f"Failed to change quantity in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data, "Failed to change quantity"
        print(f"Updated Cart in {base_url}: {data}")

# Test Case 4: Remove Item from Cart
def test_remove_from_cart(user_uuid, game_uuid):
    print("\n---Testing Remove Item from Cart---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_14), (BASE_URL_DEV, HEADERS_API_14)]:
        print(f"Testing Remove Item from Cart in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/cart/remove", headers=headers, json={"item_uuid": game_uuid})
        assert response.status_code == 200, f"Failed to remove item in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data, "Failed to remove item"
        print(f"Updated Cart in {base_url}: {data}")

# Test Case 5: Clear Cart
def test_clear_cart(user_uuid):
    print("\n---Testing Clear Cart---")
    for base_url in [BASE_URL_RELEASE, BASE_URL_DEV]:
        print(f"Testing Clear Cart in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/cart/clear", headers=HEADERS_API_15)
        assert response.status_code == 200, f"Failed to clear cart in {base_url}: {response.text}"
        data = response.json()
        assert "items" in data and len(data["items"]) == 0, "Cart was not cleared"
        print(f"Cart after clearing in {base_url}: {data}")

# Example Test Execution
user_uuid = "c2c8f767-85b4-47ec-b0e0-e76aefe9e209"  # Valid user UUID
# user_uuid = "515ce5db-c923-4025-82ca-59b604e32355"  # Valid user UUID
games = ["1990ecdd-4d3d-4de2-91b9-d45d794c82bc", "0378c074-92d6-4d8c-b6d3-878c08dbe27f", "03dbad48-ad81-433d-9901-dd5332f5d9ee"]
games_1 = ["cb620f56-daa4-43e0-b4a0-e80f8e5be279", "aca79a7c-5b66-4ff2-b3b8-57e56fc053a7", "09531e2b-c3eb-4338-a002-cc4817a7cc58", "77a94eec-38e0-4a08-a3d7-2be1007ef686", "12dc6bb3-cd3f-412a-86fe-3c1dce867481", "06520f6e-5096-4d49-a044-136357737eff", "5449c9d0-3399-44e1-bd63-f6cbb62c38ea"]
all = ["1990ecdd-4d3d-4de2-91b9-d45d794c82bc", "0378c074-92d6-4d8c-b6d3-878c08dbe27f", "03dbad48-ad81-433d-9901-dd5332f5d9ee", "cb620f56-daa4-43e0-b4a0-e80f8e5be279", "aca79a7c-5b66-4ff2-b3b8-57e56fc053a7", "09531e2b-c3eb-4338-a002-cc4817a7cc58", "77a94eec-38e0-4a08-a3d7-2be1007ef686", "12dc6bb3-cd3f-412a-86fe-3c1dce867481", "06520f6e-5096-4d49-a044-136357737eff", "5449c9d0-3399-44e1-bd63-f6cbb62c38ea"]
game_uuid = "1990ecdd-4d3d-4de2-91b9-d45d794c82bc"  # Example valid game UUID
invalid_user_uuid = "invalid-user-uuid"  # Invalid user UUID
invalid_game_uuid = "invalid-game-uuid"  # Invalid game UUID

# Run the tests
# test_get_cart(user_uuid)  # Valid user UUID
# for game in all:
    # test_add_to_cart(user_uuid, game, 1)  # Valid user UUID and game UUID
    # test_remove_from_cart(user_uuid, game)  # Valid user UUID and game UUID
# test_add_to_cart(user_uuid, game_uuid, 1)  # Valid user UUID and game UUID
# test_change_in_cart(user_uuid, game_uuid, 4)  # Valid user UUID, game UUID, and quantity
# test_remove_from_cart(user_uuid, game_uuid)  # Valid user UUID and game UUID
test_clear_cart(user_uuid)  # Valid user UUID

# Invalid tests to simulate failures (for Dev environment)
# print("\n---Simulating Invalid Tests---")
# test_get_cart(invalid_user_uuid)  # Invalid user UUID
# test_add_to_cart(invalid_user_uuid, game_uuid)  # Invalid user UUID and valid game UUID
# test_remove_from_cart(invalid_user_uuid, invalid_game_uuid)  # Invalid user UUID and invalid game UUID
