from services.base_service import get, post, put, delete

def test_get_comments():
    comments = get('comments')
    assert len(comments) > 0, "No comments returned."
    assert 'postId' in comments[0], "Comments do not contain 'postId'."
    assert 'email' in comments[0], "Comments do not contain 'email'."
    assert 'body' in comments[0], "Comments do not contain 'body'."

def test_post_comment():
    new_comment = {"postId": 1, "name": "New Comment", "email": "test@test.com", "body": "Comment content"}
    response = post('comments', new_comment)
    assert response['body'] == new_comment['body']

def test_put_comment():
    updated_comment = {"postId": 1, "name": "Updated Comment", "email": "test@test.com", "body": "Updated content"}
    response = put('comments/1', updated_comment)
    assert response['body'] == updated_comment['body']

def test_delete_comment():
    status_code = delete('comments/1')
    assert status_code == 200, "Failed to delete comment."