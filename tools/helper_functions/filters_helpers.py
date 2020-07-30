import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from tools.global_data import *
from tools.ex_conds import *
import random
import string
from .custom_functions import *


def filter_helpers_shelter_default_check(self):
    element_visible(self, FilterBar.shelter)
    element_click(self, FilterBar.shelter)
    amenities_check(self, "Shelter")


def filter_helpers_amenities_list(filter_type):
    amenities_list = []
    if filter_type == "Hygiene":
        amenities_list.append("Showers")
        amenities_list.append("Laundry")
        amenities_list.append("Diapers")
        amenities_list.append("Hygiene")
        amenities_list.append('Kits')
        amenities_list.append("Personal")
        amenities_list.append("Supplies")
        amenities_list.append("Toiletries")
    elif filter_type == "Clothes":
        amenities_list.append('Clothing')
        amenities_list.append("Clothes")
    elif filter_type == "Transit":
        amenities_list.append("Transitional")
        amenities_list.append("Buss")
        amenities_list.append("Passes")
        amenities_list.append("Transportation")
    elif filter_type == "Assistance":
        amenities_list.append("Advocacy")
        amenities_list.append("Legal")
        amenities_list.append('Services')
        amenities_list.append("Assistance")
        amenities_list.append("Rental")
        amenities_list.append("Utility")
    elif filter_type == "Resources":
        amenities_list.append("Advocacy")
        amenities_list.append("Services")
        amenities_list.append("Assistance")
        amenities_list.append("Rental")
        amenities_list.append("Utility")
        amenities_list.append(" Assistance")
        amenities_list.append("Transitional")
        amenities_list.append("Buss")
        amenities_list.append("Passes")
        amenities_list.append("Transportation")
        amenities_list.append("Vouchers")
        amenities_list.append('Clothing')
        amenities_list.append("Clothes")
        amenities_list.append("Showers")
        amenities_list.append("Laundry")
        amenities_list.append("Diapers")
        amenities_list.append("Kits")
        amenities_list.append("Supplies")
        amenities_list.append("Toiletries")
    elif filter_type == "Education":
        amenities_list.append("Education")
        amenities_list.append("Outreach")
        amenities_list.append("School")
        amenities_list.append("Program")
        amenities_list.append("Training")
    elif filter_type == "Employment":
        amenities_list.append("Training")
        amenities_list.append("Employment")
        amenities_list.append("Job")
        amenities_list.append("Education")
        amenities_list.append("Mentoring")
        amenities_list.append("Work")
    elif filter_type == "Work":
        amenities_list.append("Education")
        amenities_list.append("Outreach")
        amenities_list.append("Education")
        amenities_list.append("Program")
        amenities_list.append("Training")
        amenities_list.append("Job")
        amenities_list.append("Employment")
        amenities_list.append("Mentoring")
    elif filter_type == "Medical":
        amenities_list.append("Clinic")
        amenities_list.append("HIV")
        amenities_list.append("Syringe")
        amenities_list.append("Testing")
        amenities_list.append("Medical")
        amenities_list.append("prescriptions")
        amenities_list.append("health")
        amenities_list.append("clinic")
        amenities_list.append("Well")
        amenities_list.append("Immunizations")
        amenities_list.append("immunizations")
        amenities_list.append("Dental")
        amenities_list.append("Health")
    elif filter_type == "Counseling":
        amenities_list.append("Counseling")
        amenities_list.append("Substance")
        amenities_list.append("Therapy")
        amenities_list.append("Treatment")
        amenities_list.append("Mental")
        amenities_list.append("Behavior")
        amenities_list.append("Behavioral")
        amenities_list.append("Counseling")
    elif filter_type == "Health":
        amenities_list.append("Clinic")
        amenities_list.append("HIV")
        amenities_list.append("Syringe")
        amenities_list.append("Clinic")
        amenities_list.append("Medical")
        amenities_list.append("prescriptions")
        amenities_list.append("health")
        amenities_list.append("clinic")
        amenities_list.append("Urgent")
        amenities_list.append("Well")
        amenities_list.append("Immunizations")
        amenities_list.append("immunizations")
        amenities_list.append("Dental")
        amenities_list.append("Health")
        amenities_list.append("Counseling")
        amenities_list.append("Substance")
        amenities_list.append("Therapy")
        amenities_list.append("Treatment")
        amenities_list.append("Mental")
        amenities_list.append("Behavior")
        amenities_list.append("Behavioral")
        amenities_list.append("Counseling")
    elif filter_type == "Soup Kitchens":
        amenities_list.append("Meals")
        amenities_list.append("Soup")
        amenities_list.append("Dinner")
        amenities_list.append("Breakfast")
        amenities_list.append("Lunch")
    elif filter_type == "Food Pantries":
        amenities_list.append("Bank")
        amenities_list.append("Boxes")
        amenities_list.append("Food")
        amenities_list.append("Pantries")
        amenities_list.append("Pantry")
        amenities_list.append("Meals")
    elif filter_type == "Food":
        amenities_list.append("Bank")
        amenities_list.append("Boxes")
        amenities_list.append("Food")
        amenities_list.append("Pantries")
        amenities_list.append("Pantry")
        amenities_list.append("Meals")
        amenities_list.append("Soup")
        amenities_list.append("Dinner")
        amenities_list.append("Breakfast")
        amenities_list.append("Lunch")
        amenities_list.append("more")
    elif filter_type == "Emergency":
        amenities_list.append("Emergency")
        amenities_list.append("Shelter")
        amenities_list.append("Housing")
        amenities_list.append("shelter")
        amenities_list.append("housing")
        amenities_list.append("Shelter")
        amenities_list.append("Safe")
    elif filter_type == "Transitional":
        amenities_list.append('Shelter')
        amenities_list.append("Day")
        amenities_list.append("Night")
        amenities_list.append("Evening")
        amenities_list.append("Housing")
        amenities_list.append("housing")
        amenities_list.append("Transitional")
        amenities_list.append("Living")
        amenities_list.append("Care")
        amenities_list.append("Safe")
    elif filter_type == "Shelter":
        amenities_list.append("Day")
        amenities_list.append("Night")
        amenities_list.append("Evening")
        amenities_list.append("Shelter")
        amenities_list.append("Housing")
        amenities_list.append("housing")
        amenities_list.append("Transitional")
        amenities_list.append("Emergency")
        amenities_list.append("Housing")
        amenities_list.append("shelter")
        amenities_list.append("housing")
        amenities_list.append("Shelter")
        amenities_list.append("Care")
        amenities_list.append("Safe")
        amenities_list.append("shelter")
    return amenities_list
