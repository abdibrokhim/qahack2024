import requests

def test_user_list_offset():
    headers = {
        "Authorization": "Bearer qahack2024:abdibrokhim@gmail.com",
        "X-Task-Id": "api-6"
    }
    params = {"offset": 0}
    
    # Should pass on release
    response = requests.get(
        "https://release-gs.qa-playground.com/api/v1/users",
        headers=headers,
        params=params
    )
    print('response:', response.json())
    t = response.json()["offset"] == 10
    print("Test user_list_offset: ", t)


# Run all tests
def run_tests():
    test_user_list_offset()


if __name__ == "__main__":
    run_tests()