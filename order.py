import requests

# Set up for both environments
BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

# Headers for various APIs
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

HEADERS_API_16 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-16"
}

HEADERS_API_17 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-17"
}

HEADERS_API_18 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-18"
}

# Test Case 1: Create a new order
def test_create_order(user_uuid, item_uuid, quantity):
    print("\n---Testing Create Order---")
    order_data = {
        "items": [
            {
                "item_uuid": item_uuid,
                "quantity": quantity
            }
        ]
    }
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_16), (BASE_URL_DEV, HEADERS_API_16)]:
        print(f"Testing Create Order in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/orders", headers=headers, json=order_data)
        assert response.status_code == 200, f"Failed to create order in {base_url}: {response.text}"
        data = response.json()
        assert "status" in data and data["status"] == "open", "Order status is not open"
        print(f"Created Order in {base_url}: {data}")

# Test Case 2: List all orders for a user
def test_list_orders(user_uuid):
    print("\n---Testing List Orders---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_17), (BASE_URL_DEV, HEADERS_API_17)]:
        print(f"Testing List Orders in environment: {base_url}")
        response = requests.get(f"{base_url}/users/{user_uuid}/orders", headers=headers)
        assert response.status_code == 200, f"Failed to list orders in {base_url}: {response.text}"
        data = response.json()
        assert "orders" in data, "No orders found"
        print(f"Orders for {user_uuid} in {base_url}: {data}")

# Test Case 3: Update an order status
def test_update_order_status(order_uuid, new_status):
    print("\n---Testing Update Order Status---")
    if new_status not in ["canceled"]:
        print("Invalid status for update. Status can only be changed to 'canceled'.")
        return
    
    status_data = {
        "status": new_status
    }
    for base_url, headers in [(BASE_URL_DEV, HEADERS_API_18), (BASE_URL_DEV, HEADERS_API_18)]:
        print(f"Testing Update Order Status in environment: {base_url}")
        response = requests.patch(f"{base_url}/orders/{order_uuid}/status", headers=headers, json=status_data)
        assert response.status_code == 200, f"Failed to update order status in {base_url}: {response.text}"
        data = response.json()
        assert "status" in data and data["status"] == new_status, f"Order status not updated to {new_status}"
        print(f"Updated Order Status to {new_status} in {base_url}: {data}")

# Example Test Execution
user_uuid = "515ce5db-c923-4025-82ca-59b604e32355"  # Valid user UUID
order_uuid = "8d54e02a-dd34-4280-8ded-53eb780b6992"  # Example order UUID
item_uuid = "5449c9d0-3399-44e1-bd63-f6cbb62c38ea"  # Example valid game UUID
quantity = 2  # Example quantity

# Run the tests
# test_create_order(user_uuid, item_uuid, quantity)  # Create a new order
test_list_orders(user_uuid)  # List orders for the user
# test_update_order_status(order_uuid, "canceled")  # Update order status to 'canceled'

# Simulate invalid update to an order status (attempting an invalid status)
# test_update_order_status(order_uuid, "completed")  # Attempt to change to an invalid status