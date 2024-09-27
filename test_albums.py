# tests/test_albums.py
from services.base_service import get, post, put, delete

def test_get_albums():
    albums = get('albums')
    assert len(albums) > 0, "No albums returned."
    assert 'userId' in albums[0], "Albums do not contain 'userId'."
    assert 'title' in albums[0], "Albums do not contain 'title'."

def test_post_album():
    new_album = {"userId": 1, "title": "New Album"}
    response = post('albums', new_album)
    assert response['title'] == new_album['title']

def test_put_album():
    updated_album = {"userId": 1, "title": "Updated Album"}
    response = put('albums/1', updated_album)
    assert response['title'] == updated_album['title']

def test_delete_album():
    status_code = delete('albums/1')
    assert status_code == 200, "Failed to delete album."