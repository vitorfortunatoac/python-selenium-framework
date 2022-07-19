import sys
import pytest
from pages.TheInternetPages.DropDownPage import DropDownPage
# Requirements:
# The user should access http://the-internet.herokuapp.com/dropdown
# The user should select `Option 1`
# The user should check if the `Option 1` is selected
# The user should select `Option 2`
# The user should check if the `Option 2` is selected

sys.path.append("..")
@pytest.mark.skip(reason="Example disabled")
@pytest.mark.parametrize("driver", ["http://the-internet.herokuapp.com/dropdown"], indirect=True)
def test_change_dropdown_options(driver):
    DropDownPage(driver).select_option_by_text() \
        .is_correct_option_selected()
    DropDownPage(driver).select_option_by_text(option = "Option 1") \
            .is_correct_option_selected(option = "Option 1")

