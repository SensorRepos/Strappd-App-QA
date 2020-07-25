import unittest
from appium import webdriver
from tools.ex_conds import *
from tools.desired_capabilities import *
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep


class FiltersWorkTest(unittest.TestCase, ResetCapabilities):
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_0_skip_onboarding(self):
        get_through_onboarding(self)

    def test_1a_shelter_defaulted_as_selected(self):
        # Shelter defaults as the selected filter
        amenities_check(self, FilterBar.shelter)

    def test_2a_work_filter(self):
        # Select Work Filter Option
        amenities_check(self, FilterBar.work)
        # in sort bar All is defaulted as selected, also listed is Education and Employment
        Action.element_visible(Action, Sort.education)
        Action.element_visible(Action, Sort.employment)

    def test_2b_education_sort(self):
        # Select Education
        # In amenities list Education words are listed "Education", "Education and Outreach", "Education Assistance", ""After School Program", "Education and Training",
        amenities_check(self, Sort.education)

    def test_2c_employment_sort(self):
        # Select Employment
        # Employment words are in the Amenities list, "Job Training", "Employment Counseling", "Employment Training", "Education and Training", "Mentoring", "Life Skills and Job Training", "Employment Assistance"
        amenities_check(self, Sort.employment)


if __name__ == '__main__':
    unittest.main()
