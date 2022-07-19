"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from pages.AutomationPracticePages.BaseHeader import BaseHeader
from pages.AutomationPracticePages.ItemPage import ItemPage
from ..By import *

class HomePage(BaseHeader):
    __IMAGE_LOGO_CLASS = "img-responsive"
    __SEARCH_FIELD_ID = "search_query_top"
    __AUTO_COMPLETE_RESUT_XPATH = "//div[@class='ac_results']/ul/li"

    def __init__(self, driver):
        super().__init__(driver)
        self._find_element_by_class(self.__IMAGE_LOGO_CLASS)

    def fill_search_input(self, term_to_be_searched = "shirt"):
        
        element = self._find_element_by_id(self.__SEARCH_FIELD_ID)
        self._fill_input(element, term_to_be_searched)
        return self

    def select_auto_complete_item_by_term_containing(self, term = "T-shirts > Faded Short"):   
        auto_complete_list = self._find_element_list_by_xpath(self.__AUTO_COMPLETE_RESUT_XPATH)
        i = 0
        while i < len(auto_complete_list):
            if term in auto_complete_list[i].text:
                auto_complete_list[i].click()
            i=+1
        return ItemPage(self.driver)