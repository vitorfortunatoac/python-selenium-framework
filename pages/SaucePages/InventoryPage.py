"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from pages.BasePage import BasePage

class InventoryPage(BasePage):
    
    __INVENTORY_CONTAINER_ID = "inventory_container"

    def __init__(self, driver):        
        super().__init__(driver)
        self._find_element_by_id(self.__INVENTORY_CONTAINER_ID)