import sys
import pytest
from pages.AutomationPracticePages.HomePage import HomePage

sys.path.append("..")

@pytest.mark.parametrize("driver", ["http://automationpractice.com/index.php"], indirect=True)
@pytest.mark.skip(reason="Example disabled")
def test_success_uploaded(driver):
    HomePage(driver).fill_search_input() \
        .select_auto_complete_item_by_term_containing() \
        .is_description_correct()
