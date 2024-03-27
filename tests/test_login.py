import pytest

from source.functions import Login


@pytest.fixture(scope='session')
def login():
    login = Login()
    login.connect_to_website()


def test_valid_login(login):
    pass
def test_vxalid_login(login):
    pass