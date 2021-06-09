import logging

import time

from features.steps.steps_general import global_variable
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class General_Functions:

    driver = None

    def implicit_wait_visible(self, locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located(locator))
            logging.info("Element Visible")

        except TimeoutException:
            logging.error("Element no visible")

    def click_element(self, locator):
        try:
            General_Functions.implicit_wait_visible(self, locator)
            self.driver.find_element(*locator).click()

        except:
            raise ValueError("Element no clickable")

    def click_element_list(self, locator, row=0):
        try:
            General_Functions.implicit_wait_visible(self, locator)
            elements = self.driver.find_elements(*locator)
            size = len(elements)
            if row == 0:
                elements[size-size].click()

            else:
                print(size)
                print(size+row)
                elements[size+row].click()
        except:
            raise ValueError('Element no clickable')


    def type_text(self, locator, text):
        try:
            General_Functions.implicit_wait_visible(self, locator)
            element = self.driver.find_element(*locator)
            length =len(element.get_attribute('value'))
            element.send_keys(length * Keys.BACKSPACE)
            element.send_keys(text)
        except:
            raise ValueError("Element no interactable")

    def move_to_element(self, locator1, locator2):
        menu_element = self.driver.find_element(*locator1)
        submenu_element = self.driver.find_element(*locator2)
        build = ActionChains(self.driver)
        build.move_to_element(menu_element).click(submenu_element).perform()

    def document_ready_state(self):
        for i in range(0,10):
            status = self.driver.execute_script("return document.readyState")
            if status == "complete":
                logging.info("Page loaded")
                break
            else:
                time.sleep(2)

