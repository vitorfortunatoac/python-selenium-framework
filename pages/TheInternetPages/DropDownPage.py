"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.support.ui import Select

from pages.BasePage import BasePage

class DropDownPage(BasePage):
    
    __OPTIONS_DROPDOWN_ID = 'dropdown'
    __SELECTED_OPTION_XPATH = '//*[@selected="selected"]'

    def __init__(self, driver):        
        super().__init__(driver)
        self._find_element_by_id(self.__OPTIONS_DROPDOWN_ID)

    def select_option_by_text(self, option="Option 2"):
        dropdown = Select(self._find_element_by_id(self.__OPTIONS_DROPDOWN_ID))
        dropdown.select_by_visible_text(option)
        return self
        
    def is_correct_option_selected(self, option="Option 2"):
        selected_option = self._find_element_by_xpath(self.__SELECTED_OPTION_XPATH)
        assert selected_option.text == option

        

