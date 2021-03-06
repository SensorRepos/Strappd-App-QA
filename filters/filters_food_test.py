import unittest
from appium import webdriver
from tools.ex_conds import *
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep


class FiltersFoodTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'deviceName': 'Android',
            'app': PATH('..\\tools\\app\\org.strappd.apk'),
            "appPackage": "org.strappd",
            "appActivity": ".MainActivity",
            "ignoreUnimportantViews": "true",
            "autoGrantPermissions": "true",
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_0_skip_onboarding(self):
        get_through_onboarding(self) #copy everything to here for new pages i guess

    def test_1a_shelter_defaulted_as_selected(self):
        # Shelter defaults as the selected filter
        amenities_check(self, FilterBar.shelter)

    def test_2a_food_filter(self):
        # Select Food Filter
        # List Updates
        # Sort Options default with All Selected with Soup Kitches and Food Pantries as options
        amenities_check(self, FilterBar.food)
        element_visible(self, Sort.soup_kitchen)
        element_visible(self, Sort.food_pantries)

    def test_2b_soup_kitchen(self):
        # Select Soup Kitchen
        # In amenities list Kitchen words are listed. (Meals, Soup Kitchen, Dinner, Breakfast, Lunch""
        amenities_check(self, Sort.soup_kitchen)

    def test_2c_food_pantries(self):
        # Select Food Pantries
        # food words are in the Resources list, "Food Bank". "Food Boxes", "Food", "Pantries", "Pantry"
        amenities_check(self, Sort.food_pantries)


if __name__ == '__main__':
    unittest.main()
