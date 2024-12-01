# **QA Testing Report: API Testing (Dev vs Release Environments)**

## part 1

**Overview**:  
This report outlines the discrepancies found between the **dev** and **release** environments, based on the results of various API tests conducted on both environments. The key issues include data mismatches, incorrect status codes, pagination errors, and system failures such as internal server errors (500).

---

### **Test Case 1: API-3 - Create a New User**

- **Issue**:  
  In the dev environment, when a username already exists, the system saves the user with an empty username, while the email validation works correctly. In the release environment, the system correctly identifies both username and email as already existing and prevents user creation.
- **Expected Behavior**:  
  Both environments should prevent the creation of users with existing usernames and emails, and return appropriate error messages.
- **Actual Behavior**:  
  - **Dev Environment**: Allows user creation with an empty username, though email validation works fine.
  - **Release Environment**: Prevents creation of user if username or email already exists, returning specific errors.

---

### **Test Case 2: API-22 - Create a New User**

- **Issue**:  
  The dev environment returns a 500 internal server error each time a new user is created. The release environment works fine and creates the user successfully.
- **Expected Behavior**:  
  Both environments should allow user creation and return success messages.
- **Actual Behavior**:  
  - **Dev Environment**: Returns a 500 internal server error.
  - **Release Environment**: Successfully creates the user.

---

### **Test Case 3: API-21 - List All Users**

- **Issue**:  
  The dev environment returns an empty list of users (total: 0), while the release environment returns a list with 10 users.
- **Expected Behavior**:  
  Both environments should return the same number of users.
- **Actual Behavior**:  
  - **Dev Environment**: Returns 0 users.
  - **Release Environment**: Returns 10 users.

---

### **Test Case 4: API-6 - List All Users (Pagination Issue)**

- **Issue**:  
  - When the offset is set to 0, both environments return the correct list of users.  
  - When the offset is set to 10 in the dev environment, it returns all users again, while the release environment returns an empty list.
- **Expected Behavior**:  
  Both environments should return an empty list when offset is greater than the total number of users (i.e., offset=10).
- **Actual Behavior**:  
  - **Dev Environment**: Returns all users again at offset 10.
  - **Release Environment**: Returns an empty list at offset 10.

---

### **Test Case 5: API-23 - Get User by UUID**

- **Issue**:  
  The dev environment returns incorrect user data, with mismatched UUIDs and user details compared to the actual data. The release environment returns the correct user data.
- **Expected Behavior**:  
  Both environments should return the same user data for a given UUID.
- **Actual Behavior**:  
  - **Dev Environment**: Returns incorrect user data (UUID mismatch).
  - **Release Environment**: Returns correct user data.

---

### **Test Case 6: API-1 - Delete User by UUID**

- **Issue**:  
  The dev environment returns a 500 internal server error when attempting to delete a user by UUID, while the release environment deletes the user successfully.
- **Expected Behavior**:  
  Both environments should delete the user successfully and return a success message.
- **Actual Behavior**:  
  - **Dev Environment**: Returns a 500 internal server error.
  - **Release Environment**: Successfully deletes the user.

---

### **Test Case 7: API-7 - Get User by Credentials**

- **Issue**:  
  The dev environment returns a 404 "Not Found" error when attempting to get a user by credentials, while the release environment works fine.
- **Expected Behavior**:  
  Both environments should return the user data when valid credentials are provided.
- **Actual Behavior**:  
  - **Dev Environment**: Returns a 404 "Not Found" error.
  - **Release Environment**: Returns correct user data.

---

### **Test Case 8: API-9 - Get a Game by UUID**

- **Issue**:  
  The dev environment returns a 404 "Not Found" error when attempting to get a game by its UUID, while the release environment returns the game data correctly.
- **Expected Behavior**:  
  Both environments should return the correct game data for a valid UUID.
- **Actual Behavior**:  
  - **Dev Environment**: Returns a 404 "Not Found" error.
  - **Release Environment**: Returns the correct game data.

---

### **Test Case 9: API-10 - Get Games by Category**

- **Issue**:  
  In the dev environment, pagination with limit=5 and offset=0 returns 3 games, while the release environment returns only 1 game. The release environment also returns a 404 error for some test cases with pagination, suggesting issues with the routing or filtering mechanism.
- **Expected Behavior**:  
  Both environments should return the correct number of games based on the category, with pagination handled correctly.
- **Actual Behavior**:  
  - **Dev Environment**: Returns 3 games instead of 5.
  - **Release Environment**: Returns only 1 game and occasionally a 404 error for invalid cases.

---

### **Bug Summary**:

1. **Internal Server Errors**: Found in dev environment for multiple endpoints (e.g., user creation and deletion).
2. **Data Mismatches**: UUIDs and user data are mismatched between dev and release environments, leading to incorrect results.
3. **Pagination Errors**: Dev environment returns inconsistent results with pagination, while release environment handles pagination correctly.
4. **404 Errors**: Several APIs (e.g., get user by credentials and get game by UUID) return 404 errors in the dev environment when they should not.

---

### **Conclusion & Recommendations**:

- The dev environment exhibits significant data and functionality discrepancies compared to the release environment.
- Immediate action should be taken to investigate the internal server errors (500), as well as the data synchronization issues between environments.
- Ensure that both environments handle pagination correctly and that all API responses (especially with UUIDs) are consistent across environments.
- Additional logging and error handling should be added in the dev environment to assist in diagnosing and resolving issues more effectively.

---

## part 2

1. **API-25: Add Item to User's Wishlist**
   - **Issue in dev:** Same item added twice to wishlist.
   - **Expected Behavior:** The item should only be added once, even if the request is repeated.
   - **Suggested Fix:** Implement validation to check for duplicate items before adding them to the wishlist.

2. **API-5: Add Item to User's Wishlist**
   - **Issue in dev:** Error 422 with message "Wishlist limit is reached: 10".
   - **Expected Behavior:** Items should be added to the wishlist unless the limit is exceeded.
   - **Suggested Fix:** Verify that the wishlist limit is not reached in the dev environment and ensure correct handling of this limit.

3. **API-8: Remove Item from User's Wishlist**
   - **Issue in dev:** Item removal does not work.
   - **Expected Behavior:** The item should be removed from the wishlist.
   - **Suggested Fix:** Investigate the backend logic to ensure the item is properly removed from the wishlist in the dev environment.

4. **API-11: Update User's Avatar**
   - **Issue in dev:** Avatar update fails.
   - **Expected Behavior:** The avatar should be updated successfully.
   - **Suggested Fix:** Check for any configuration or permission issues related to file uploads or user data handling in the dev environment.

5. **API-12: List All Items in User's Cart**
   - **Issue in dev:** Total price is not calculated (still 0).
   - **Expected Behavior:** The total price should update according to the items in the cart.
   - **Suggested Fix:** Review cart update logic to ensure total price is calculated and updated correctly in the dev environment.

6. **API-13: Change Item in User's Cart**
   - **Issue in dev:** Cart does not update.
   - **Expected Behavior:** The cart should reflect changes in item quantity and total price.
   - **Suggested Fix:** Investigate API failure or data synchronization issues in the dev environment.

7. **API-14: Remove Item from User's Cart**
   - **Issue in dev:** All items removed from the cart, not just the selected one.
   - **Expected Behavior:** Only the selected item should be removed.
   - **Suggested Fix:** Review cart removal logic and ensure it targets the correct item.

8. **API-16: Create a New Order**
   - **Issue in dev:** Duplicate orders are being created.
   - **Expected Behavior:** Only one order should be created per request.
   - **Suggested Fix:** Check for race conditions or repeated API calls leading to duplicate orders in the dev environment.

9. **API-17: List All Orders for a User**
   - **Status:** No issues observed in either environment.

10. **API-18: Change Order Status**
    - **Issue in dev:** Order status update fails.
    - **Expected Behavior:** The order status should update based on the API request.
    - **Suggested Fix:** Investigate the status transition logic and ensure permissions and conditions are correctly handled in the dev environment.

11. **API-19: Get a Payment by UUID**
    - **Status:** No issues observed in either environment.

12. **API-20: Create Payment**
    - **Issue in dev:** Returns error 422 with message "Operation forbidden. Order status: payment can be created only for an order with status 'open'".
    - **Expected Behavior:** Payments should only be created for orders with status ‘open’.
    - **Suggested Fix:** Ensure the order status is ‘open’ in the dev environment before attempting to create payments.

13. **API-2: Search Game**
    - **Issue in dev:** Returns a list of all games instead of filtering by the search query.
    - **Expected Behavior:** The search query should return relevant results (e.g., filtering games based on title).
    - **Suggested Fix:** Verify the search query handling and ensure it is correctly filtering results in the dev environment.

14. **API-24: Update a User**
    - **Status:** No issues observed in either environment.

15. **API-4: Update a User**
    - **Status:** No issues observed in either environment.

---

### **Summary of Key Issues**

| **API** | **Issue in dev** | **Status in release** | **Suggested Fix** |
|---------|-------------------|-----------------------|-------------------|
| API-25  | Same item added twice to wishlist | Works as expected | Prevent duplicate items in wishlist |
| API-5   | Wishlist limit error (422) | Works as expected | Verify wishlist limits and item count |
| API-8   | Item removal not working | Works as expected | Investigate backend logic |
| API-11  | Avatar update fails | Works as expected | Investigate file permissions and API config |
| API-12  | Total price not updated | Works as expected | Check cart total price calculation logic |
| API-13  | Cart not updating | Works as expected | Investigate API failure or sync issues |
| API-14  | Removes all items from cart | Works as expected | Ensure removal targets the specific item |
| API-16  | Duplicate orders | Works as expected | Prevent duplicate order creation |
| API-18  | Order status not updating | Works as expected | Check status transition logic |
| API-20  | Payment creation fails due to order status | Works as expected | Ensure correct order status before payment |
| API-2   | Search returns all games | Filters correctly | Ensure search query is applied correctly |
| API-24  | No issues | No issues | - |
| API-4   | No issues | No issues | - |

---