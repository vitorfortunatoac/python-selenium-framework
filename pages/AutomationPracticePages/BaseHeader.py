"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from time import sleep
from pages.AutomationPracticePages.ContactUsPage import ContactUsPage
from pages.BasePage import BasePage
from ..By import *

class BaseHeader(BasePage):
    __IMAGE_LOGO_CLASS = "img-responsive"
    __SEARCH_FIELD_ID = "search_query_top"
    __AUTO_COMPLETE_RESUT_XPATH = "//div[@class='ac_results']/ul/li"

    __CONTACT_US_LINK_BUTTON_ID = "//div[@id='contact-link']/a"

    def __init__(self, driver):
        super().__init__(driver)
        self._find_element_by_class(self.__IMAGE_LOGO_CLASS)
        self._find_element_by_id(self.__SEARCH_FIELD_ID)
        self.wait_for_element_be_clickable_by_id(self.__CONTACT_US_LINK_BUTTON_ID)

    def fill_search_input(self, term_to_be_searched = "shirt"):
        element = self._find_element_by_id(self.__SEARCH_FIELD_ID)
        self._fill_input(element, term_to_be_searched)
        return self

    def click_contact_us_link_button(self):
        sleep(1)
        self._find_element_by_xpath(self.__CONTACT_US_LINK_BUTTON_ID).click()
        return ContactUsPage(self.driver)

    def select_auto_complete_item_by_term_containing(self, term = "T-shirts > Faded Short"):   
        auto_complete_list = self._find_element_list_by_xpath(self.__AUTO_COMPLETE_RESUT_XPATH)
        i = 0
        while i < len(auto_complete_list):
            if term in auto_complete_list[i].text:
                auto_complete_list[i].click()
            i=+1