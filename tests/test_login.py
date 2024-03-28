import pytest

from source.functions import login_instance


def test_valid_credentials(login_instance):
    """ This test is checking valid credentials to login (username and password from config.json)"""
    login_instance.connect_to_website()
    x = login_instance.get_login_status()
    assert x  # Should be True to approve we get in to account.


@pytest.mark.parametrize("username, password", [
    ('dummy', 'dummy'),
    ('admin', 'dummy'),
    ('dummy', 'admin123')
])
def test_invalid_credentials(login_instance, username, password):
    """ This test is checking Invalid credentials to login by 3 scenarios:
     1. Incorrect Username and Password.
     2. Correct Username and Incorrect Password.
     3. Incorrect Username and Correct Password.
     """
    login_instance.connect_to_website(username=username, password=password)
    x = login_instance.get_login_status()
    assert not x  # Should be False to approve we didn't get in to account.


@pytest.mark.parametrize("username, password, expected", [
    ('dummy', '', 1),
    ('', 'admin123', 1),
    ('', '', 2)
])
def test_empty_credentials(login_instance, username, password, expected):
    """ This test is checking Empty credentials for login by 3 scenarios:
     1. Incorrect Username and Empty Password.
     2. Empty Username and correct Password.
     3. Empty Username and Empty Password.
     """
    login_instance.connect_to_website(username=username, password=password)
    x = login_instance.get_login_fields_required_error()
    assert x == expected  # Should be as expected number of display "Required" error.


def test_ui_username_password_exists(login_instance):
    """ This test check if the UI including the Username And Password information ."""
    user, password = login_instance.get_username_and_password_from_ui()
    assert user == 'Username : Admin', "Incorrect Username"
    assert password == 'Password : admin123', "Incorrect password"


def test_forget_password_element(login_instance):
    """ This test check that you are redirect to reset password page """
    url = login_instance.get_forget_password_element()
    assert "requestPasswordResetCode" in url
