from flask import url_for


def test_index(client):
    assert client.get(url_for('main.index')).status_code == 200
