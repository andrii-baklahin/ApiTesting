import requests
import pytest
from utils import models

LU = models.LIST_USERS()


class TestListUser:

    def test_wright_data(self):
        assert (LU.users_count() / LU.page_count()) == LU.per_page()

    @pytest.mark.parametrize('page', [i for i in range(LU.page_count())])
    def test_per_page(self, page):
        per_page = LU.get_page(page)['per_page']
        real_per_page = len(LU.get_page(page)['data'])
        assert per_page == real_per_page
