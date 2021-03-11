from selenium.webdriver.common.by import By

origin = (By.XPATH, "//input[@id='origin']")
destination = (By.XPATH, "//input[@id='destination']")
click_text = (By.XPATH, "//*[contains(text(),'{0}')]")
btn_submit = (By.XPATH, "//button[@type='submit']")
calendar = (By.XPATH, "//input[@id='first-input']")
calendar_sum_day_start = (By.XPATH, "//button[@aria-label='Sumar día fecha ida']")
calendar_sum_day_end = (By.XPATH, "//button[@aria-label='Sumar día fecha vuelta']")
prices = (By.XPATH, "//tbody[@id='listaTrenesTBodyIda']/tr[1]/td[5]/button[1]")
btn_continue = (By.ID, "buttonBannerContinuar")

#calendar_days_start = (By.XPATH, "//div[contains(@class, 'lightpick__day is-available')]")
#calendar_days_ends = (By.XPATH, "//div[contains(@class, 'lightpick__day is-available is-in-range')]")

