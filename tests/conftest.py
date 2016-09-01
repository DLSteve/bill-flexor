from flask import current_app
import pytest


@pytest.fixture(scope="module")
def app():
    app = current_app
    return app