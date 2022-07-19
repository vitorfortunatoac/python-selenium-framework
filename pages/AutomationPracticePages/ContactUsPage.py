"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.support.ui import Select

from pages.BasePage import BasePage
from ..By import *

class ContactUsPage(BasePage):

    __SUBJECT_HEADER_ID = "id_contact"
    __ATTACH_FILE_INPUT_ID = "fileUpload"
    __MESSAGE_INPUT_ID = "message"
    __EMAIL_ADDRESS_INPUT_ID = "email"
    __ORDER_REFERENCE_INPUT_ID = "id_order"
    __SUBMIT_BUTTON_ID = "submitMessage"
    __ALERT_MESSAGE_ID = "alert-success"

    def select_heading_item(self, option = "Webmaster"):
        dropdown = Select(self._find_element_by_id(self.__SUBJECT_HEADER_ID))
        dropdown.select_by_visible_text(option)
        return self
    
    def fill_email_field(self, email="test@test.com"):
        self._fill_input(self._find_element_by_id(self.__EMAIL_ADDRESS_INPUT_ID), email)
        return self
    
    def attach_image(self, image="blank.png"):
        self.file_uploader_from_resource(self._find_element_by_id(self.__ATTACH_FILE_INPUT_ID), image)
        return self

    def fill_message_field(self, message="Any message"):
        self._fill_input(self._find_element_by_id(self.__MESSAGE_INPUT_ID), message)
        return self

    def fill_order_reference_field(self, order_reference="1313"):
        self._fill_input(self._find_element_by_id(self.__ORDER_REFERENCE_INPUT_ID), order_reference)
        return self

    def click_to_submit(self):
        self._find_element_by_id(self.__SUBMIT_BUTTON_ID).click()
        return self

    def is_form_sent_successfully(self, message = "Your message has been successfully sent to our team."):
        self.is_element_containing_text(self._find_element_by_id(self.__ALERT_MESSAGE_ID), message)