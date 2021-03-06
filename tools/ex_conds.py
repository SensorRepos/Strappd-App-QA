from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_cond

def element_to_be_clickable(self,locator):
    element = WebDriverWait(self.driver, 20).until(ex_cond.element_to_be_clickable(locator)).is_enabled()

def element_click(self, locator):
    element = WebDriverWait(self.driver, 20).until(ex_cond.element_to_be_clickable(locator)).click()


def element_invisible(self, locator):
    element = WebDriverWait(self.driver, 60).until(ex_cond.invisibility_of_element_located(locator))


def element_visible(self, locator):
    element = WebDriverWait(self.driver, 20).until(ex_cond.visibility_of_element_located(locator))


def get_text_from_element(self, locator):
    element = WebDriverWait(self.driver, 20).until(ex_cond.presence_of_element_located(locator)).text
    return element


def element_has_text(self, locator, text):
    element = WebDriverWait(self.driver, 20).until(ex_cond.text_to_be_present_in_element(locator, text))


def element_send_text(self, locator, text):
    element = WebDriverWait(self.driver, 20).until(ex_cond.element_to_be_clickable(locator)).send_keys(text)

def element_to_be_clickable(self,locator):
    element = WebDriverWait(self.driver, 20).until(ex_cond.element_to_be_clickable(locator)).is_enabled()