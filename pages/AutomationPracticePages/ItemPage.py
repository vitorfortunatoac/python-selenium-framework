"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from pages.AutomationPracticePages.BaseHeader import BaseHeader
from ..By import *

class ItemPage(BaseHeader):

    __SHORT_DESCRIPTION_ID = "short_description_block"
    __BASE_DESCRIPTION_TEXT = "Faded short sleeve t-shirt with high neckline. Soft and stretchy material for a comfortable fit. Accessorize with a straw hat and you're ready for summer!"

    def is_description_correct(self, description = __BASE_DESCRIPTION_TEXT):
        assert self._find_element_by_id(self.__SHORT_DESCRIPTION_ID).text == description