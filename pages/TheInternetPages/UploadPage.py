"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from pages.BasePage import BasePage

class UploadPage(BasePage):
    
    __FILE_SUBMIT_BUTTON_ID = "file-submit"
    __FILE_UPLOAD_INPUT_ID = "file-upload"
    __DRAG_AND_DROP_INPUT_ID = "drag-drop-upload"
    __FILE_UPLOADED_MESSAGE_ID = "uploaded-files"

    def __init__(self, driver):        
        super().__init__(driver)
        self._find_element_by_id(self.__FILE_SUBMIT_BUTTON_ID)
        self._find_element_by_id(self.__FILE_UPLOAD_INPUT_ID)
        self._find_element_by_id(self.__DRAG_AND_DROP_INPUT_ID)

    def upload_file(self):
        element = self._find_element_by_id(self.__FILE_UPLOAD_INPUT_ID)
        return self.file_uploader_from_resource(element, "blank.png")

    def click_to_upload_file_button(self):
        self._find_element_by_id(self.__FILE_SUBMIT_BUTTON_ID).click()
        return self

    def is_file_uploaded(self):
        self.is_element_containing_text(self \
            ._find_element_by_id(self.__FILE_UPLOADED_MESSAGE_ID), "blank.png")