"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .By import *

class BasePage:
    __ROOT_DIR = os.path.abspath(os.curdir)
    
    def __init__(self, driver):
        self.driver = driver
        self.__BASE_DRIVER_WAIT = WebDriverWait(self.driver, 10)

    def _find_element_by_text(self, text, elementType = "*"):
        try:
            element = self.driver.find_element(By.XPATH, f"//{elementType}[contains(text(),\'{text}')]")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element
        except Exception as Error :
            raise Exception(f"Element //{elementType}[contains(text(),\'{text}')] not found:\n{Error}'")

    def _find_element_by_id(self, id):
        try:
            element = self.driver.find_element(By.ID, id)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element
        except Exception as Error :
            raise Exception(f"Element not found:\n{Error}'")
    def wait_for_element_be_clickable_by_id(self, xpath):
        try:
            element = self.__BASE_DRIVER_WAIT.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return element
        except Exception as Error :
            raise Exception(f"Element not found:\n{Error}'")        
        
    def _find_element_by_class(self, class_name):
        try:
            
            element = self.driver.find_element(By.CLASS_NAME, class_name)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element
        except Exception as Error :
            raise Exception(f"Element not found:\n{Error}'")  

    def _find_element_list_by_xpath(self, xpath):
        try:
            element = self.driver.find_elements(By.XPATH, xpath)
            return element
        except Exception as Error :
            raise Exception(f"Element not found:\n{Error}'")
    def _find_element_list_by_id(self, id):
        try:
            element = self.driver.find_elements(By.ID, id)
            return element
        except Exception as Error :
            raise Exception(f"Element not found:\n{Error}'")

    def _find_element_by_custom_matcher(self, custom_matcher, id):
        try:
            element = self.driver.find_element(By.XPATH, f'//*[@{custom_matcher}="{id}"]')
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element
        except Exception as Error :
            raise Exception(f"Element not found:\n{Error}'")

    def _fill_input(self, element, text):
        try:
            element.clear()
            if not text == True:
                element.send_keys(text)
            return self
        except Exception as Error :
            raise Exception(f"Element not found:\n{Error}'")

    def _find_element_by_xpath(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element
        except Exception as Error :
            raise Exception(f"Element not found:\n{Error}'")
    
    def is_element_containing_text(self, element, text):
        try:
            assert element.text == text
            # return element
        except Exception as Error :
            raise Exception(f"Message `{element.text}` does not match with expected `{text}`:\n{Error}'")

    def is_element_containing_attribute(self, element, attribute, other_attr):
        try:
            return other_attr in element.get_attribute(attribute)
        except Exception as Error :
            raise Exception(f"Message `{element.get_attribute(attribute)}` does not match with expected `{other_attr}`:\n{Error}'")

    def file_uploader_from_resource(self, element, resource_element):
        try:
            resource_path = f"{self.__ROOT_DIR}/resources/{resource_element}"
            element.send_keys(resource_path)
            return self
        except Exception as Error :
            raise Exception(f"We couldn't attach resource\n{resource_path}\n{Error}")