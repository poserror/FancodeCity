from services.base_service import get, post, put, delete

def test_get_posts():
    posts = get('posts')
    assert len(posts) > 0, "No posts returned."
    assert 'userId' in posts[0], "Posts do not contain 'userId'."
    assert 'title' in posts[0], "Posts do not contain 'title'."
    assert 'body' in posts[0], "Posts do not contain 'body'."

def test_post_post():
    new_post = {"userId": 1, "title": "New Post", "body": "Post content"}
    response = post('posts', new_post)
    assert response['title'] == new_post['title']

def test_put_post():
    updated_post = {"userId": 1, "title": "Updated Post", "body": "Updated content"}
    response = put('posts/1', updated_post)
    assert response['title'] == updated_post['title']

def test_delete_post():
    status_code = delete('posts/1')
    assert status_code == 200, "Failed to delete post."