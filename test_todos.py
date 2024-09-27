from services.base_service import get, post, put, delete

def test_get_todos():
    todos = get('todos')
    assert len(todos) > 0, "No todos returned."
    assert 'userId' in todos[0], "Todos do not contain 'userId'."
    assert 'title' in todos[0], "Todos do not contain 'title'."
    assert 'completed' in todos[0], "Todos do not contain 'completed'."

def test_post_todo():
    new_todo = {"userId": 1, "title": "New Task", "completed": False}
    response = post('todos', new_todo)
    assert response['title'] == new_todo['title']

def test_put_todo():
    updated_todo = {"userId": 1, "title": "Updated Task", "completed": True}
    response = put('todos/1', updated_todo)
    assert response['title'] == updated_todo['title']

def test_delete_todo():
    status_code = delete('todos/1')
    assert status_code == 200, "Failed to delete todo."