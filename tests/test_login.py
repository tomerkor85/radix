import pytest

from source.functions import Login


@pytest.fixture()
def login():
    login_instance = Login()
    login_instance.connect_to_website()
    yield login_instance  # Yield the Login instance so it can be used in tests


def test_valid_login(login):
    # Your test code here
    pass


def test_invalid_login(login):
    # Your test code here
    pass
