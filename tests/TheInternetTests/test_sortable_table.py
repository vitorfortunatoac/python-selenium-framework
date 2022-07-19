import sys
import pytest
from pages.TheInternetPages.DataTablePage import DataTablePage

sys.path.append("..")
# Requirements:
# The user should access http://the-internet.herokuapp.com/tables
# The user should sort by ascending `due`
# The user should verify if the table is sorted by ascending
# The user should sort by descending `due`
# The user should verify if the table is sorted by descending

@pytest.mark.parametrize("driver", ["http://the-internet.herokuapp.com/tables"], indirect=True)
@pytest.mark.skip(reason="Example disabled")
def test_validate_sort(driver):
    DataTablePage(driver).table_sort_by_descending_due_colunm()\
        .is_listed_sorted_by_due()

    DataTablePage(driver).table_sort_by_ascending_due_colunm().\
        is_listed_sorted_by_due(is_ascending=True)
