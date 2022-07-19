import sys
import pytest
from pages.SaucePages.InventoryPage import InventoryPage
from pages.SaucePages.LoginPage import LoginPage
sys.path.append("..")

__VALID_PASSWORD = "secret_sauce"
__INVALID_PASSWORD = "invalid_secret_sauce"
__VALID_USERNAME = "standard_user"
__LOCKED_USERNAME = "locked_out_user"
__INVALID_USERNAME = "invalid_user"
# MESSAGES
__WRONG_CREDENTIALS_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
__MISSING_PASSWORD_ERROR_MESSAGE = "Epic sadface: Password is required"
__MISSING_USERNAME_ERROR_MESSAGE = "Epic sadface: Username is required"
__LOCKED_USER_ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
# Requirements:
# The user should use `standard_user`
# The user should use `secret_sauce` as a valid password
# The user should be redirected to Inventory Page
@pytest.mark.skip(reason="Example disabled")
def test_success_login(driver):
    LoginPage(driver).fill_username_input(__VALID_USERNAME) \
        .fill_password_field(__VALID_PASSWORD) \
        .click_in_login_button()

    InventoryPage(driver)

@pytest.mark.skip(reason="Example disabled")
def test_required_login_username_field(driver):
    LoginPage(driver).click_in_login_button() \
        .is_error_message_visible_with_text(__MISSING_USERNAME_ERROR_MESSAGE)

    LoginPage(driver).fill_username_input(__VALID_USERNAME) \
        .click_in_login_button() \
        .is_error_message_visible_with_text(__MISSING_PASSWORD_ERROR_MESSAGE)

@pytest.mark.skip(reason="Example disabled")
def test_locked_user(driver):
    LoginPage(driver).fill_username_input(__LOCKED_USERNAME) \
        .fill_password_field(__VALID_PASSWORD) \
        .click_in_login_button() \
        .is_error_message_visible_with_text(__LOCKED_USER_ERROR_MESSAGE)

@pytest.mark.skip(reason="Example disabled")
def test_required_login_password_field(driver):
    LoginPage(driver).fill_username_input() \
        .fill_password_field(__VALID_PASSWORD) \
        .click_in_login_button() \
        .is_error_message_visible_with_text(__MISSING_USERNAME_ERROR_MESSAGE)

@pytest.mark.skip(reason="Example disabled")
def test_wrong_credentials(driver):
    LoginPage(driver).fill_username_input(__INVALID_USERNAME) \
        .fill_password_field(__INVALID_PASSWORD) \
        .click_in_login_button() \
        .is_error_message_visible_with_text(__WRONG_CREDENTIALS_ERROR_MESSAGE)

    LoginPage(driver).fill_username_input(__VALID_USERNAME) \
        .fill_password_field(__INVALID_PASSWORD) \
        .click_in_login_button() \
        .is_error_message_visible_with_text(__WRONG_CREDENTIALS_ERROR_MESSAGE)

    LoginPage(driver).fill_username_input(__INVALID_USERNAME) \
        .fill_password_field(__VALID_PASSWORD) \
        .click_in_login_button() \
        .is_error_message_visible_with_text(__WRONG_CREDENTIALS_ERROR_MESSAGE)
