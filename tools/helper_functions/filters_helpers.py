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
        amenities_list.append("Hygiene Kits")
        amenities_list.append("Personal Supplies")
        amenities_list.append("Toiletries")
    elif filter_type == "Clothes":
        amenities_list.append('Clothing')
        amenities_list.append('Cloths for kids')
        amenities_list.append("Clothes")
    elif filter_type == "Transit":
        amenities_list.append("Transitional Assistance")
        amenities_list.append("Transitional")
        amenities_list.append("Buss Pass")
        amenities_list.append("Buss Passes")
        amenities_list.append("Transportation")
        amenities_list.append("Transportation Vouchers")
        amenities_list.append("Transitional Living Program")
    elif filter_type == "Assistance":
        amenities_list.append("Advocacy")
        amenities_list.append("Legal Services")
        amenities_list.append("Assistance")
        amenities_list.append("Rental Assistance")
        amenities_list.append("Utility Assistance")
    elif filter_type == "Resources":
        amenities_list.append("Advocacy")
        amenities_list.append("Legal Services")
        amenities_list.append("Assistance")
        amenities_list.append("Rental Assistance")
        amenities_list.append("Utility Assistance")
        amenities_list.append("Transitional Assistance")
        amenities_list.append("Transitional")
        amenities_list.append("Buss Pass")
        amenities_list.append("Buss Passes")
        amenities_list.append("Transportation")
        amenities_list.append("Transportation Vouchers")
        amenities_list.append('Clothing')
        amenities_list.append('Cloths for kids')
        amenities_list.append("Clothes")
        amenities_list.append("Showers")
        amenities_list.append("Laundry")
        amenities_list.append("Diapers")
        amenities_list.append("Hygiene Kits")
        amenities_list.append("Personal Supplies")
        amenities_list.append("Toiletries")
    elif filter_type == "Education":
        amenities_list.append("Education")
        amenities_list.append("Education and Outreach")
        amenities_list.append("Education Assistance")
        amenities_list.append("After School Program")
        amenities_list.append("Education and Training")
    elif filter_type == "Employment":
        amenities_list.append("Job Training")
        amenities_list.append("Employment Counseling")
        amenities_list.append("Employment Training")
        amenities_list.append("Education and Training")
        amenities_list.append("Mentoring")
        amenities_list.append("Life Skills and Job Training")
        amenities_list.append("Employment Assistance")
    elif filter_type == "Work":
        amenities_list.append("Education")
        amenities_list.append("Education and Outreach")
        amenities_list.append("Education Assistance")
        amenities_list.append("After School Program")
        amenities_list.append("Education and Training")
        amenities_list.append("Job Training")
        amenities_list.append("Employment Counseling")
        amenities_list.append("Employment Training")
        amenities_list.append("Education and Training")
        amenities_list.append("Mentoring")
        amenities_list.append("Life Skills and Job Training")
        amenities_list.append("Employment Assistance")
        amenities_list.append("Workforce Development & more")
        amenities_list.append("Workforce Development")
    elif filter_type == "Medical":
        amenities_list.append("Clinic")
        amenities_list.append("HIV Testing")
        amenities_list.append("Syringe Access")
        amenities_list.append("Medical Clinic")
        amenities_list.append("Medical")
        amenities_list.append("prescriptions")
        amenities_list.append("health")
        amenities_list.append("clinic")
        amenities_list.append("Urgent Medical Assistance")
        amenities_list.append("Well Child Checks,")
        amenities_list.append("Immunizations")
        amenities_list.append("immunizations")
        amenities_list.append("Dental")
        amenities_list.append("Health")
    elif filter_type == "Counseling":
        amenities_list.append("Counseling")
        amenities_list.append("Substance Abuse Treatment")
        amenities_list.append("Therapy")
        amenities_list.append("Treatment")
        amenities_list.append("Mental Health")
        amenities_list.append("Behavior")
        amenities_list.append("Behavioral")
        amenities_list.append("Counseling & more")
    elif filter_type == "Health":
        amenities_list.append("Clinic")
        amenities_list.append("HIV Testing")
        amenities_list.append("Syringe Access")
        amenities_list.append("Medical Clinic")
        amenities_list.append("Medical")
        amenities_list.append("prescriptions")
        amenities_list.append("health")
        amenities_list.append("clinic")
        amenities_list.append("Urgent Medical Assistance")
        amenities_list.append("Well Child Checks,")
        amenities_list.append("Immunizations")
        amenities_list.append("immunizations")
        amenities_list.append("Dental")
        amenities_list.append("Health")
        amenities_list.append("Counseling")
        amenities_list.append("Substance Abuse Treatment")
        amenities_list.append("Therapy")
        amenities_list.append("Treatment")
        amenities_list.append("Mental Health")
        amenities_list.append("Behavior")
        amenities_list.append("Behavioral")
        amenities_list.append("Counseling & more")
    elif filter_type == "Soup Kitchens":
        amenities_list.append("Meals")
        amenities_list.append("Soup Kitchen")
        amenities_list.append("Dinner")
        amenities_list.append("Breakfast")
        amenities_list.append("Lunch")
    elif filter_type == "Food Pantries":
        amenities_list.append("Food Bank")
        amenities_list.append("Food Boxes")
        amenities_list.append("Food")
        amenities_list.append("Pantries")
        amenities_list.append("Pantry")
        amenities_list.append("Meals")
    elif filter_type == "Food":
        amenities_list.append("Food Bank")
        amenities_list.append("Food Boxes")
        amenities_list.append("Food")
        amenities_list.append("Pantries")
        amenities_list.append("Pantry")
        amenities_list.append("Meals")
        amenities_list.append("Soup Kitchen")
        amenities_list.append("Dinner")
        amenities_list.append("Breakfast")
        amenities_list.append("Lunch")
    elif filter_type == "Emergency":
        amenities_list.append("Emergency")
        amenities_list.append("Emergency Shelter")
        amenities_list.append("Emergency Housing")
        amenities_list.append("Housing")
        amenities_list.append("shelter")
        amenities_list.append("housing")
        amenities_list.append("Shelter")
        amenities_list.append("Safe Place program")
    elif filter_type == "Transitional":
        amenities_list.append('Emergency Shelter')
        amenities_list.append("Day")
        amenities_list.append("Night")
        amenities_list.append("Evening")
        amenities_list.append("Day Shelter")
        amenities_list.append("Night Shelter")
        amenities_list.append("Evening Shelter")
        amenities_list.append("Housing")
        amenities_list.append("housing")
        amenities_list.append("Transitional Housing")
        amenities_list.append("Transitional Shelter")
        amenities_list.append("Transitional Living Program")
        amenities_list.append("Shelter Care")
        amenities_list.append("Safe Place program")
    elif filter_type == "Shelter":
        amenities_list.append("Day")
        amenities_list.append("Night")
        amenities_list.append("Evening")
        amenities_list.append("Day Shelter")
        amenities_list.append("Night Shelter")
        amenities_list.append("Evening Shelter")
        amenities_list.append("Housing")
        amenities_list.append("housing")
        amenities_list.append("Transitional Housing")
        amenities_list.append("Transitional Shelter")
        amenities_list.append("Emergency")
        amenities_list.append("Emergency Shelter")
        amenities_list.append("Emergency Housing")
        amenities_list.append("Housing")
        amenities_list.append("shelter")
        amenities_list.append("housing")
        amenities_list.append("Shelter")
        amenities_list.append("Transitional Living Program")
        amenities_list.append("Shelter Care")
        amenities_list.append("Safe Place program")
        amenities_list.append("Shelter")
        amenities_list.append("Shelter")
    return amenities_list
