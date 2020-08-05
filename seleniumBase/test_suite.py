''' NOTE: This test suite contains 2 passing tests and 2 failing tests. '''

import pytest
from seleniumbase import BaseCase


class MyTestSuite(BaseCase):
    @pytest.mark.expected_success
    def test_1(self):
        self.open("https://xkcd.com/1663/")
        self.assert_text("Garden", "div#ctitle", timeout=3)
        for p in range(4):
            self.click('a[rel="next"]')
        self.assert_text("Algorithms", "div#ctitle", timeout=3)

    @pytest.mark.expected_failure
    def test_2(self):
        print("\n(This test fails on purpose)")
        self.open("https://xkcd.com/1675/")
        raise Exception("FAKE EXCEPTION: This test fails on purpose.")

    @pytest.mark.expected_success
    def test_3(self):
        self.open("https://xkcd.com/1406/")
        self.assert_text("Universal Converter Box", "div#ctitle", timeout=3)
        self.open("https://xkcd.com/608/")
        self.assert_text("Form", "div#ctitle", timeout=3)

    @pytest.mark.expected_failure
    def test_4(self):
        print("\n(This test fails on purpose)")
        self.open("https://xkcd.com/1670/")
        self.assert_element("FakeElement.DoesNotExist", timeout=0.5)

    @pytest.mark.visual_test
    def test_xkcd_layout_change(self):
        self.open('https://xkcd.com/554/')
        print('\nCreating baseline in "visual_baseline" folder.')
        self.check_window(name="xkcd_554", baseline=True)
        # Change height: (83 -> 130) , Change width: (185 -> 120)
        self.set_attribute('[alt="xkcd.com logo"]', "height", "130")
        self.set_attribute('[alt="xkcd.com logo"]', "width", "120")
        self.check_window(name="xkcd_554", level=0)

