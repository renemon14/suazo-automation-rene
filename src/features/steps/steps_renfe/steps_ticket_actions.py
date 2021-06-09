import time
from behave import *
from selenium.webdriver.common.keys import Keys

from elements import page_renfe_index, page_renfe_billete
from functions import general_functions

function = general_functions.General_Functions()

@step('Accept cookies all')
def step_impl(self):
    function.click_element(page_renfe_index.cookies)
    time.sleep(4)


@step('Go to section: "{section}"')
def step_impl(self, section):
    function.document_ready_state()
    if section == "Viajar-Tarifas-Billetes":
        function.move_to_element(page_renfe_index.menu_viajar,
                                 page_renfe_index.menu_billetes)


@step('I want to go from "{origin}" to "{destination}"')
def step_impl(self, origin, destination):
    function.type_text(page_renfe_billete.origin, origin)

    function.click_element((page_renfe_billete.click_text[0],
                            page_renfe_billete.click_text[1].format(origin)))

    function.type_text(page_renfe_billete.destination, destination)
    function.click_element((page_renfe_billete.click_text[0],
                            page_renfe_billete.click_text[1].format(destination)))


@step('Select date in calendar')
def step_impl(self):
    function.click_element(page_renfe_billete.calendar)
    self.driver.find_element(*page_renfe_billete.calendar_sum_day_start).send_keys(Keys.ENTER * 10)
    self.driver.find_element(*page_renfe_billete.calendar_sum_day_end).send_keys(Keys.ENTER * 4)
    time.sleep(5)


@step('Submit')
def step_impl(self):
    function.click_element(page_renfe_billete.btn_submit)


@step('Select basic price round trip')
def step_impl(self):
    time.sleep(2)
    function.click_element(page_renfe_billete.prices)
    function.click_element(page_renfe_billete.btn_continue)
