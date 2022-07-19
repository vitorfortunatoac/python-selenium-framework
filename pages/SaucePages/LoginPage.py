"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
import time
from pages.BasePage import BasePage
from ..By import *

class LoginPage(BasePage):
    __CLOSE_ERROR_MESSAGE_FIELD_CLASS = "error-button"
    __USERNAME_FIELD_ID = "user-name"
    __PASSWORD_FIELD_ID = "password"
    __LOGIN_BUTTON_ID = "login-button"
    __ERROR_MESSAGE_FIELD_DATA_TEST = "error"

    def click_in_login_button(self):
        self._find_element_by_id(self.__LOGIN_BUTTON_ID).click()
        return self

    def close_error_message(self):
        self._find_element_by_class(self.__CLOSE_ERROR_MESSAGE_FIELD_CLASS).click()
        return self

    def fill_username_input(self, username = ""):
        element = self._find_element_by_id(self.__USERNAME_FIELD_ID)
        return self._fill_input(element, username)

    def fill_password_field(self, password = ""):
        element = self._find_element_by_id(self.__PASSWORD_FIELD_ID)
        return self._fill_input(element, password)

    def click_la(self):
        time.sleep(5)
        self._find_element_by_id(self.__USERNAME_FIELD_ID).click()
        return self

    def is_error_message_visible_with_text(self, erro_text):
        requiredFieldContainer = self \
            ._find_element_by_custom_matcher(By.DATA_TEST, self.__ERROR_MESSAGE_FIELD_DATA_TEST)
        self.is_element_containing_text(requiredFieldContainer, erro_text)