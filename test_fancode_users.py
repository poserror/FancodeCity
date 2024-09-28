import pytest
from services.todo_service import get_todos_by_user, completed_task_percentage
from services.user_service import get_users, get_fancode_users

def test_all_users():
    users = get_users()  # Fetch all users
    fancode_users = get_fancode_users(users)
    required_completed_percentage = 50 # Define the complete percentage based on the testcase 
    if not users:
        print("No users found or there was an error fetching users.")
        return
    
    failed_users = []
    for user in fancode_users:

        todos = get_todos_by_user(user['id'])  # Fetch todos for each FanCode user
        if not todos:
            print(f"Skipping user {user['id']} due to missing or failed todos data.")
            continue  # Skip to the next user if fetching todos failed
        completion_percentage = completed_task_percentage(todos)
        print(f"\nCompletion percentage for user {user['name']} is {completion_percentage}%.")

        # Using assert to check the completion percentage
        if completion_percentage < required_completed_percentage:
            failed_users.append(user['name'])

    # If there are users with completion percent less than required, fail the testcase
    if len(failed_users) > 0:
        pytest.fail(f"{failed_users}")    
    