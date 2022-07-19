import sys
import pytest
from pages.TheInternetPages.UploadPage import UploadPage
sys.path.append("..")

@pytest.mark.parametrize("driver", ["http://the-internet.herokuapp.com/upload"], indirect=True)
@pytest.mark.skip(reason="Example disabled")
def test_success_uploaded(driver):
    UploadPage(driver).upload_file() \
        .click_to_upload_file_button() \
        .is_file_uploaded()
