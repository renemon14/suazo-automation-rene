import time
from behave import *


global_variable = {}

@step('Site to navigate: "{url}"')
def step_impl(self, url):
    self.driver.get(url)
    global_variable['driver'] = self.driver



@step('Wait "{seg}" seconds')
def step_impl(self, seg):
    time.sleep(int(seg))