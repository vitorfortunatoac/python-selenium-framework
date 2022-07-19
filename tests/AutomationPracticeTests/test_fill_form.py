import sys
import time
import pytest
from pages.AutomationPracticePages.HomePage import HomePage

sys.path.append("..")
# Requirements:
# The user should access http://automationpractice.com/index.php
# The user should click in the `Contact Us` button
# The user should include order reference `R108`
# The user should include the email `test@test.com`
# The user should include the message `This is a test`
# The user should include an `blank.png` image
# The user should submit and validate the success message

@pytest.mark.parametrize("driver", ["http://automationpractice.com/index.php"], indirect=True)
@pytest.mark.skip(reason="Example disabled")
def test_fill_form(driver):
    
    HomePage(driver).click_contact_us_link_button() \
        .select_heading_item() \
        .fill_email_field() \
        .fill_message_field() \
        .fill_order_reference_field() \
        .attach_image() \
        .click_to_submit()
