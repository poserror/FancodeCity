from services.base_service import get, post, put, delete

def test_get_users():
    users = get('users')
    assert len(users) > 0, "No users returned."
    assert 'username' in users[0], "Users do not contain 'username'."
    assert 'email' in users[0], "Users do not contain 'email'."
    assert 'address' in users[0], "Users do not contain 'address'."

def test_post_user():
    new_user = {
        "name": "Abcd", "username": "abcd2", "email": "abc@gmail.com",
        "address": {"street": "123 Street", "city": "FanCode", "zipcode": "12345"}
    }
    response = post('users', new_user)
    assert response['username'] == new_user['username']

def test_put_user():
    updated_user = {
        "name": "X", "username": "xyz", "email": "x.y@gmail.com",
        "address": {"street": "456 Street", "city": "FanCode", "zipcode": "67890"}
    }
    response = put('users/1', updated_user)
    assert response['username'] == updated_user['username']

def test_delete_user():
    status_code = delete('users/1')
    assert status_code == 200, "Failed to delete user."
