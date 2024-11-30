import requests

BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

headers = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-6"
}

# Test 1: Check if the 'offset' query parameter works correctly
def test_offset_param():
    params = {"offset": 10}
    
    # Test for the release environment
    response = requests.get(f"{BASE_URL_RELEASE}/users", headers=headers, params=params)
    assert response.status_code == 200, f"Failed on release: {response.text}"
    assert response.json().get("offset") == 10, f"Offset incorrect on release: {response.text}"

    # Test for the dev environment (should fail if there's a bug)
    response = requests.get(f"{BASE_URL_DEV}/users", headers=headers, params=params)
    assert response.status_code == 200, f"Failed on dev: {response.text}"
    assert response.json().get("offset") == 10, f"Offset incorrect on dev (expected bug): {response.text}"

# Test 2: Fetch a category by UUID
def test_get_category():
    category_uuid = "8126d35b-5336-41ad-981d-f245c3e05665"  # Replace with an actual UUID for testing
    
    # Test for the release environment
    response = requests.get(f"{BASE_URL_RELEASE}/categories/{category_uuid}", headers=headers)
    assert response.status_code == 200, f"Failed on release: {response.text}"
    category = response.json()
    assert category["uuid"] == category_uuid, f"UUID mismatch on release: {response.text}"

    # Test for the dev environment (should fail if there's a bug)
    response = requests.get(f"{BASE_URL_DEV}/categories/{category_uuid}", headers=headers)
    assert response.status_code == 200, f"Failed on dev: {response.text}"
    category = response.json()
    assert category["uuid"] == category_uuid, f"UUID mismatch on dev (expected bug): {response.text}"

# Test 3: Add an item to the cart
def test_add_to_cart():
    user_uuid = "00000000-0000-4562-b3fc-2c963f66afa6"  # Replace with an actual UUID for testing
    item_uuid = "00000000-0000-4562-b3fc-2c963f66afa6"  # Replace with an actual item UUID
    quantity = 1
    
    # Prepare cart item data
    cart_item = {
        "item_uuid": item_uuid,
        "quantity": quantity
    }

    # Test for the release environment
    cart_data = {
        "user_uuid": user_uuid,
        "items": [cart_item]
    }
    response = requests.post(f"{BASE_URL_RELEASE}/carts", headers=headers, json=cart_data)
    assert response.status_code == 201, f"Failed on release: {response.text}"
    cart = response.json()
    assert len(cart["items"]) == 1, f"Unexpected number of items in cart on release: {response.text}"

    # Test for the dev environment (should fail if there's a bug)
    response = requests.post(f"{BASE_URL_DEV}/carts", headers=headers, json=cart_data)
    assert response.status_code == 201, f"Failed on dev: {response.text}"
    cart = response.json()
    assert len(cart["items"]) == 1, f"Unexpected number of items in cart on dev (expected bug): {response.text}"

# Test 4: Fetch game details by UUID
def test_get_game():
    game_uuid = "1990ecdd-4d3d-4de2-91b9-d45d794c82bc"  # Replace with an actual game UUID
    
    # Test for the release environment
    response = requests.get(f"{BASE_URL_RELEASE}/games/{game_uuid}", headers=headers)
    assert response.status_code == 200, f"Failed on release: {response.text}"
    game = response.json()
    assert game["uuid"] == game_uuid, f"UUID mismatch on release: {response.text}"

    # Test for the dev environment (should fail if there's a bug)
    response = requests.get(f"{BASE_URL_DEV}/games/{game_uuid}", headers=headers)
    assert response.status_code == 200, f"Failed on dev: {response.text}"
    game = response.json()
    assert game["uuid"] == game_uuid, f"UUID mismatch on dev (expected bug): {response.text}"

# Running all tests
def run_tests():
    # test_offset_param()
    test_get_category()
    # test_add_to_cart()
    # test_get_game()

if __name__ == "__main__":
    run_tests()