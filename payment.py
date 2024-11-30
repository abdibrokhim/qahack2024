import requests

# Set up for both environments
BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"

HEADERS_API_19 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-19"
}

HEADERS_API_20 = {
    "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
    "X-Task-Id": "api-20"
}


# Test Case 1: Get a payment by UUID
def test_get_payment(payment_uuid):
    print("\n---Testing Get Payment---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_19), (BASE_URL_DEV, HEADERS_API_19)]:
        print(f"Testing Get Payment in environment: {base_url}")
        response = requests.get(f"{base_url}/payments/{payment_uuid}", headers=headers)
        assert response.status_code == 200, f"Failed to get payment in {base_url}: {response.text}"
        data = response.json()
        assert "uuid" in data and data["uuid"] == payment_uuid, f"Payment UUID mismatch in {base_url}"
        print(f"Payment details in {base_url}: {data}")

# Test Case 2: List all payments for a user
def test_list_payments(user_uuid):
    print("\n---Testing List Payments---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_20), (BASE_URL_DEV, HEADERS_API_20)]:
        print(f"Testing List Payments in environment: {base_url}")
        response = requests.get(f"{base_url}/users/{user_uuid}/payments", headers=headers)
        assert response.status_code == 200, f"Failed to list payments in {base_url}: {response.text}"
        data = response.json()
        assert "payments" in data, "No payments found"
        print(f"Payments for {user_uuid} in {base_url}: {data}")

# Test Case 3: Create a new payment for an order
def test_create_payment(user_uuid, order_uuid, payment_method):
    print("\n---Testing Create Payment---")
    payment_data = {
        "order_uuid": order_uuid,
        "payment_method": payment_method
    }
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_19), (BASE_URL_DEV, HEADERS_API_19)]:
        print(f"Testing Create Payment in environment: {base_url}")
        response = requests.post(f"{base_url}/users/{user_uuid}/payments", headers=headers, json=payment_data)
        assert response.status_code == 200, f"Failed to create payment in {base_url}: {response.text}"
        data = response.json()
        assert "status" in data and data["status"] == "processing", f"Payment status is not processing"
        print(f"Created Payment in {base_url}: {data}")

# Test Case 4: Delete a payment by UUID
def test_delete_payment(payment_uuid):
    print("\n---Testing Delete Payment---")
    for base_url, headers in [(BASE_URL_RELEASE, HEADERS_API_19), (BASE_URL_DEV, HEADERS_API_19)]:
        print(f"Testing Delete Payment in environment: {base_url}")
        response = requests.delete(f"{base_url}/payments/{payment_uuid}", headers=headers)
        assert response.status_code == 204, f"Failed to delete payment in {base_url}: {response.text}"
        print(f"Payment {payment_uuid} deleted in {base_url}")

# Example Test Execution

# user_uuid = "c2c8f767-85b4-47ec-b0e0-e76aefe9e209"  # Valid user UUID
user_uuid = "515ce5db-c923-4025-82ca-59b604e32355"  # Valid user UUID
payment_uuid = "b4941796-7ccc-4ff8-9f73-ffa84ae62450"  # Example payment UUID
# order_uuid = "7f82919e-ca34-4e2d-ba28-0b417b5a5aa3"  # Example order UUID
# order_uuid = "d24bc814-db33-461f-9d1f-e0b937d212be"  # Example order UUID
order_uuid = "d3aa904e-fd4b-4b23-bbfb-b02b737d8d9f"  # Example order UUID
payment_method = "card"  # Example payment method

# Run the tests
test_get_payment(payment_uuid)  # Get a payment
# test_list_payments(user_uuid)  # List all payments for the user
# test_create_payment(user_uuid, order_uuid, payment_method)  # Create a new payment
# test_delete_payment(payment_uuid)  # Delete a payment
