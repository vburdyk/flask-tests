import requests


def test_get_articles_list():
    response = requests.get("http://nginx/api/articles")
    assert response.status_code == 200
    assert response.json()[0].get("id") == 4


def test_create_article():
    response = requests.post("http://nginx/api/articles", json={
        "title": "hello",
        "body": "hello hello hello"
    })
    assert response.status_code == 200
    assert response.json().get("title") == "hello"
    res = requests.delete("http://nginx/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 204


def test_update_article():
    response = requests.post("http://nginx/api/articles", json={
        "title": "hello",
        "body": "hello hello hello"
    })
    assert response.status_code == 200

    updated_article = {"title": "hello updated", "body": "hello hello hello updated"}
    res = requests.put("http://nginx/api/articles/" + str(response.json().get("id")), json=updated_article)
    assert res.status_code == 200

    res = requests.get("http://nginx/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 200
    assert res.json().get("title") == "hello updated"
    assert res.json().get("body") == "hello hello hello updated"

    res = requests.delete("http://nginx/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 204


def test_delete_article():
    response = requests.post("http://nginx/api/articles", json={
        "title": "hello",
        "body": "hello hello hello"
    })
    assert response.status_code == 200

    res = requests.delete("http://nginx/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 204

    res = requests.get("http://nginx/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 500


def test_get_category_list():
    response = requests.get("http://nginx/api/categories")
    assert response.status_code == 200
    assert response.json()[0].get("id") == 1


def test_get_menuitem():
    response = requests.get("http://nginx/api/menu-items")
    assert response.status_code == 200
    assert response.json()[0].get("id") == 1


def test_create_menuitem():
    response = requests.post("http://nginx/api/menu-items", json={
        "name": "hello",
        "link": "helloo"
    })
    assert response.status_code == 200
    assert response.json().get("name") == "hello"

    res = requests.delete("http://nginx/api/menu-items/" + str(response.json()["id"]))
    assert res.status_code == 404
