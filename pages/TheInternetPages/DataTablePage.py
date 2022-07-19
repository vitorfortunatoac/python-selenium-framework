"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from pages.BasePage import BasePage
from ..By import *

class DataTablePage(BasePage):
    
    __DUE_TABLE_HEADER_CLASS = "dues"
    __DUE_TABLE_DESCENDING_SORT_CLASS = "headerSortUp"
    __DUE_TABLE_ASCENDING_SORT_CLASS = "headerSortDown"
    __TABLE_COLUNMS_XPATH = "//table[@id='table2']/thead/tr/th/span"
    __TABLE_ROWS_XPATH = '//table[@id="table2"]/tbody/tr'

    def __init__(self, driver):        
        super().__init__(driver)

    def table_sort_by_ascending_due_colunm(self):
        element = self._find_element_by_class(self.__DUE_TABLE_HEADER_CLASS)
        if not self.__sort_by_clicking_element(element, self.__DUE_TABLE_ASCENDING_SORT_CLASS) == True:
            assert self.__sort_by_clicking_element(element, self.__DUE_TABLE_ASCENDING_SORT_CLASS)
        return self

    def table_sort_by_descending_due_colunm(self):
            element = self._find_element_by_class(self.__DUE_TABLE_HEADER_CLASS)
            if not self.__sort_by_clicking_element(element, self.__DUE_TABLE_DESCENDING_SORT_CLASS) == True:
                assert self.__sort_by_clicking_element(element, self.__DUE_TABLE_DESCENDING_SORT_CLASS)
            return self

    def get_element_position_in_header_by_class(self, class_name):
        element = self._find_element_list_by_xpath(self.__TABLE_COLUNMS_XPATH)
        i = 0
        while i < len(element):
            if element[i].get_attribute("class") == class_name:
                return i+1
            i+=1
        raise Exception(f"Unable to find element {class_name} in the table'")
        
    def is_listed_sorted_by_due(self, is_ascending = False):
        element = self._find_element_list_by_xpath(self.__TABLE_ROWS_XPATH)
        row_position = self.get_element_position_in_header_by_class(self.__DUE_TABLE_HEADER_CLASS)
        colunm_elements_list = []
        for colunm_element in element:
            temp_item = colunm_element.find_element(By.XPATH, f"td[{row_position}]")
            temp_item = temp_item.text.replace("$", "")
            colunm_elements_list.append(float(temp_item))
        if(colunm_elements_list == sorted(colunm_elements_list, reverse=is_ascending)):
            raise Exception(f"Not sorted. Configuration is Ascending {is_ascending}'")

    def __sort_by_clicking_element(self, element, ascendingOrDescending ):
                element.click()
                parentElement = element.find_element(By.XPATH, "..")
                return self.is_element_containing_attribute(parentElement, "class", ascendingOrDescending)