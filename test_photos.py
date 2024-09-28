from services.base_service import get, post, put, delete

def test_get_photos():
    photos = get('photos')
    print("Number of photos uploaded: ",len(photos))
    assert len(photos) > 0, "No photos returned."
    assert 'albumId' in photos[0], "Photos do not contain 'albumId'."
    assert 'title' in photos[0], "Photos do not contain 'title'."
    assert 'url' in photos[0], "Photos do not contain 'url'."

def test_post_photo():
    new_photo = {"albumId": 1, "title": "New Photo", "url": "http://example.com/photo", "thumbnailUrl": "http://example.com/thumb"}
    response = post('photos', new_photo)
    assert response['title'] == new_photo['title']

def test_put_photo():
    updated_photo = {"albumId": 1, "title": "Updated Photo", "url": "http://example.com/photo-updated", "thumbnailUrl": "http://example.com/thumb-updated"}
    response = put('photos/1', updated_photo)
    assert response['title'] == updated_photo['title']

def test_delete_photo():
    status_code = delete('photos/1')
    assert status_code == 200, "Failed to delete photo."